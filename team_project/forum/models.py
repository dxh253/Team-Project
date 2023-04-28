from django.db.models import CharField, TextField, Model, ForeignKey, URLField, IntegerField, ManyToManyField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class Category(TimeStampedModel):
    name = CharField(max_length=56, help_text='Enter category name')
    path = CharField(max_length=20, help_text='Enter category url path')
    slug = AutoSlugField(
        "category url slug",
        unique=True,
        always_update=False,
        populate_from="path")
    description = TextField("Category Description", blank=True)
    owner = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True)

    # Metadata
    class Meta:
        ordering = ['-slug']

    # Methods
    def get_absolute_url(self):
        return reverse('reddit:category', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.slug)


class Post(TimeStampedModel):
    title = CharField(max_length=100, help_text='Enter Post Title')
    description = TextField("Post Description", blank=True)
    owner = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False)
    category = ForeignKey(Category,
                        on_delete=models.CASCADE,
                        null=False)
    image = models.ImageField(upload_to='images/', default='default.png')   
    slug = AutoSlugField(
        "Post url slug",
        unique=True,
        always_update=False,
        populate_from="title")
    user_vote = 0
    user_up_style = ''
    user_down_style = ''
    isBlurred = models.BooleanField(default=False)

    class Meta:
        ordering = ['-modified']

    def get_absolute_url(self):
        return reverse('reddit:post', kwargs={'slug': self.slug, 'category_slug': self.category_slug})

    def __str__(self):
        return self.title

    def get_category(self):
        return self.category.slug

    def get_full_url(self):
        return '/r/' + self.category.slug + '/' + self.slug

    def username(self):
        return self.owner.username

    def category_name(self):
        return self.category.name

    def time_since_post(self):
        e = ''
        if self.modified != self.created:
            e = '*'
        time_now = datetime.now(timezone.utc)
        diff_time = time_now - self.modified
        diff_days, diff_hours, diff_mins = str(diff_time.days), str(
            int(diff_time.seconds / 3600)), str(int(diff_time.seconds / 60))
        if diff_days == '0':
            if int(diff_mins) < 60:
                if diff_mins == '1':
                    return e+'1 minute ago.'
                return e+diff_mins + ' minutes ago.'
            if diff_hours == '1':
                return e+'1 hour ago'
            return e+diff_hours + ' hours ago.'
        if diff_days == '1':
            return e+'1 day ago.'
        return e+diff_days + ' days ago.'

    def owner_url(self):
        return '/users/' + self.owner.username

    # def number_of_comments(self):
    #     return PostComment.objects.filter(post_id=self.id).count()

    def description_br(self):
        safe_text = self.description.replace('<', '').replace('>', '').replace(
            '{{', '').replace('{%', '').replace('}}', '').replace('%}', '')
        safe_text = safe_text.replace('((b))', '<strong>').replace(
            '((/b))', '</strong>').replace('((i))', '<i>').replace('((/i))', '</i')
        return "<br>".join(safe_text.splitlines())

    def score(self):
        votes = PostVotes.objects.filter(post_id=self.id)
        score = 0
        for vote in votes:
            score = score + vote.vote
        return score
    score = score

    def age_in_days(self):
        time_now = datetime.now(timezone.utc)
        diff_time = time_now - self.created
        days_since_post, secs_since_post = diff_time.days, diff_time.seconds
        days_since_post_float = secs_since_post / 86400 + days_since_post
        return days_since_post_float

    def weighted_score(self):
        if self.score() == 0:
            return 0
        time_now = datetime.now(timezone.utc)
        diff_time = time_now - self.created
        days_since_post, secs_since_post = diff_time.days, diff_time.seconds
        days_since_post_float = secs_since_post / 86400 + days_since_post
        return self.score() / days_since_post_float
    
    def get_image(self):
        if self.image:
            return self.image.url
        return ''

    category_slug = get_category
    full_url = get_full_url

class PostVotes(Model):
    post_id = ForeignKey('Post', related_name='post', on_delete=models.CASCADE)
    user_id = ForeignKey(settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE, null=False)
    VOTE_CHOICES = [(-1, 'downvote'), (0, 'no vote'), (1, 'upvote')]
    vote = IntegerField(choices=VOTE_CHOICES, default=None)

    def up_color(self):
        if self.vote == 1:
            return 'orange'
        return 'grey'

    def down_color(self):
        if self.vote == -1:
            return 'blue'
        return 'grey'

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='parent_comment_replies',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    upvoted_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='upvoted_comments',
        blank=True,
    )
    downvoted_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='downvoted_comments',
        blank=True,
    )

    def __str__(self):
        return self.text

    def upvote(self, user):
        if user not in self.upvoted_by.all():
            self.upvoted_by.add(user)
            self.downvoted_by.remove(user)
        else:
            self.upvoted_by.remove(user)

    def downvote(self, user):
        if user not in self.downvoted_by.all():
            self.downvoted_by.add(user)
            self.upvoted_by.remove(user)
        else:
            self.downvoted_by.remove(user)

    def is_owner(self, user):
        return self.author == user

    def can_be_deleted(self, user):
        return self.is_owner(user) or self.post.is_owner(user)

class Reply(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='comment_replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    parent_reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.body
class CommentVote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1
    VOTE_CHOICES = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='votes')
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'comment')

    def __str__(self):
        return f"{self.user.username} - {self.comment.id} - {self.vote}"


class ReplyVote(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(choices=(('up', 'Upvote'), ('down', 'Downvote')), max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reply', 'user')

    def __str__(self):
        return f'{self.vote_type}vote on {self.reply}'

from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files import File

from io import BytesIO
from PIL import Image

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    
class Thread(models.Model):
    category = models.ForeignKey(Category, related_name='forums', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forums')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    upvotes = models.ManyToManyField(User, related_name='forum_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='forum_downvotes', blank=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ('-date_added',)
        verbose_name_plural = 'forums'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''
    
    def get_thumbnail_url(self):
        if self.thumbnail:
            return self.thumbnail.url
        elif self.image:
            self.create_thumbnail()
            return self.thumbnail.url
        return ''
    
    def create_thumbnail(self, size=(300, 200)):
        if not self.image:
            return
        
        with self.image.open() as img:
            img = img.convert('RGB')
            img.thumbnail(size)

            thumb_io = BytesIO()
            img.save(thumb_io, 'JPEG', quality=85)

            thumb_name = f'{self.image.name.split(".")[0]}_thumb.jpg'
            self.thumbnail.save(thumb_name, File(thumb_io), save=False)
        
    def save(self, *args, **kwargs):
        if not self.slug:
            last_event = Thread.objects.filter(category=self.category).last()

            if last_event:
                self.slug = f'{slugify(self.title)}-{last_event.pk + 1}'
            else:
                self.slug = slugify(self.title)

            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='post_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='post_downvotes', blank=True)

    class ordering:
        ordering = ('-created',)

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return f'/{self.thread.forum.category.slug}/{self.thread.forum.slug}/{self.thread.slug}/'
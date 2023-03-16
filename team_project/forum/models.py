from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files import File

from io import BytesIO
from PIL import Image

class Forum(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

class Thread(models.Model):
    forum = models.ForeignKey(Forum, related_name='threads', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='threads', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    upvotes = models.ManyToManyField(User, related_name='upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvotes', blank=True)
    slug = models.SlugField()
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
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
            last_thread = Thread.objects.last()

            if last_thread:
                new_id = last_thread.id + 1
            else:
                new_id = 1
            
            self.slug = f'{slugify(self.title)}-{new_id}'
            
        super().save(*args, **kwargs)

class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='post_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='post_downvotes', blank=True)

    class ordering:
        ordering = ('-created',)

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return f'/{self.thread.slug}/'

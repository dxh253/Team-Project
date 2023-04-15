from io import BytesIO
from PIL import Image

from django.core.files.base import ContentFile
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Events(models.Model):
    category = models.ForeignKey(
        Category, related_name='events', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField(blank=True, null=True)
    venue = models.TextField(blank=True, null=True)
    date = models.DateField()
    image = models.ImageField()
    thumbnail = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='events', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return ''

    def save(self, *args, **kwargs):
        if not self.slug:
            # If the instance is new and the slug is not set, generate a new slug
            last_event = Events.objects.last()

            # Generate a new slug based on the last instance's ID + 1
            if last_event:
                new_id = last_event.id + 1
            else:
                new_id = 1

            self.slug = slugify(f"{new_id}-{self.name}")

        super().save(*args, **kwargs)

    def delete_event(self, user=None, *args, **kwargs):
        super().delete(*args, **kwargs)


class UserEvent(models.Model):
    user = models.ForeignKey(
        User, related_name='saved_events', on_delete=models.CASCADE)
    event = models.ForeignKey(
        Events, related_name='saved_by_users', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f'{self.user.username} saved {self.event.name}'

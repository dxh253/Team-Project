from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.utils.text import slugify


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
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

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

        # Open the image using PIL
        with self.image.open() as img:
            # Convert to RGB
            img = img.convert('RGB')
            # Resize the image
            img.thumbnail(size)

            # Create a BytesIO object to write the thumbnail to
            thumb_io = BytesIO()
            # Save the resized image to the BytesIO object
            img.save(thumb_io, 'JPEG', quality=85)

            # Create a new thumbnail file from the BytesIO object
            thumb_name = f'{self.image.name.split(".")[0]}_thumb.jpg'
            self.thumbnail.save(thumb_name, File(thumb_io), save=False)

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

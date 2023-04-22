from django.db import models

from django.conf import settings

# Create your models here.

class Problems(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='problems', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

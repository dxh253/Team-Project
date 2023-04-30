from django.db import models

from django.conf import settings

# Create your models here.


class Problems(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='problems', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    def delete_problem(self, user=None, *args, **kwargs):
        super().delete(*args, **kwargs)

    def author(self):
        return self.owner.username


class Comment(models.Model):
    problem = models.ForeignKey(
        Problems, on_delete=models.CASCADE, related_name="pcomments",)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='pcomments', on_delete=models.CASCADE, null=False)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.text

    def username(self):
        return self.author.username

    def date(self):
        return self.created_date.date()

    def delete_comment(self, user=None, *args, **kwargs):
        super().delete(*args, **kwargs)

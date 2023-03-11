from django.db import models


class StudyGroup(models.Model):
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    meeting_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

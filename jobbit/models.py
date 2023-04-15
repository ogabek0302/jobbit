from django.db import models
from django.utils import timezone


class Job(models.Model):
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)

    id = models.AutoField(primary_key=True) # add this field

    def __str__(self):
        return self.title

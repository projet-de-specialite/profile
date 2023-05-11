from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=255)
    bio = models.TextField()
    website = models.CharField(max_length=255)
    avatar = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.username

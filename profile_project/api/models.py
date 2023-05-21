from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
import os

class Profile(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=255)
    bio = models.TextField()
    website = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to=os.environ.get('IMAGES_PATH'))
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.id)])

    
    @classmethod
    def create(cls, user_id, name, birth_date, bio, website, avatar):
        profile = cls(user_id=user_id, name=name, birth_date=birth_date, bio=bio, website=website, avatar=avatar)
        profile.save()
        return profile


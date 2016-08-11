from __future__ import unicode_literals

from django.db import models
from uuslug import uuslug
from django.contrib.auth.models import User

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    views = models.IntegerField(default=0)
    slug = models.CharField(max_length=100, unique=True)
    
    def __unicode__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title.lower(), instance=self, max_length=100)
        super(Post, self).save(*args, **kwargs)

class UserProfile(models.Model):
    #Class to allow adding additional user fields
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True, null=True)
    

    def __unicode__(self):
        return self.user.username
    
class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    
    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.content[:30]))
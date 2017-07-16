from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    # additional fields
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    feedback = models.TextField(blank=True)

    def __str__(self) :
        return self.user.username


class userName(models.Model):
    name = models.CharField(max_length=254,unique=True)

    def __str__(self):
        return self.name

class mfeedBack(models.Model):
    mentorName = models.ForeignKey(userName)
    mentorResponse=models.TextField(max_length=1000)

    def __str__(self):
        return self.mentorResponse

class bfeedBack(models.Model):
    buddyName = models.ForeignKey(userName)
    buddyResponse=models.TextField(max_length=1000)

    def __str__(self):
        return self.buddyResponse

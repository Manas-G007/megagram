from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Currently user model
User=get_user_model()

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(default="hey, I'm using megagram")
    profileimg=models.ImageField(upload_to='profile_images',default='dp.png')
    location=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

class PostTest(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    userPro=models.ImageField(upload_to='post_userPro',default="")
    image=models.ImageField(upload_to='post_image')
    caption=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)      

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower=models.CharField(max_length=100)
    user=models.CharField(max_length=100)

    def __str__(self):
        return self.user

class chatContent(models.Model):
    sender=models.CharField(max_length=100)
    reciever=models.CharField(max_length=100)
    message=models.CharField(max_length=500)
    time=models.TimeField(default=datetime.now().time())

    def __self__(self):
        return self.sender

class Comments(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)
    comment=models.CharField(max_length=250)
    dummyPro=models.ImageField(upload_to='dummyPro',default="")

    def __self__(self):
        return self.username
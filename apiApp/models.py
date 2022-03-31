import re
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validate(self, form):
        errors = {}

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] ='Sorry that username has been taken please chose a different one'
        
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'That email is already being used'

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Please use a valid email format'

        if len(form['password']) < 6:
            errors['password'] = 'Password must be at least 5 characters long'
        
        if form['password'] != form['confirm']:
            errors['password'] = 'Password do not match'

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    userCreatedAt = models.DateTimeField(auto_now_add=True)
    userUpdatedAt = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    def __str__(self):
        return f'{self.firstName} {self.lastName}'

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profileImgs', default='bee.jpeg')
    def __str__(self):
        return f'{self.user.username} Profile'

def create_user_profile(sender, instance, created, **kwargs):
    
    if created:
        User.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)

class Favorite(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='userFavs', on_delete=CASCADE)
    def __str__(self):
        return self.name

class Upload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    img = models.FileField(upload_to='images', default='bee.jpeg')
    user = models.ForeignKey(User, related_name='userUploads', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Forecast(models.Model):
    city = models.CharField(max_length=255)
    conditions = models.CharField(max_length=255)
    temp = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='userForcast', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

from django.db import models
import re
from django.db.models.deletion import CASCADE
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Sorry that email is already in the system'
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Please use  a valid email address'
        if len(form['password']) < 6:
            errors['password'] = 'Password must be at least 6 characters'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        
        return errors
    
class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    userCreatedAt = models.DateTimeField(auto_now_add=True)
    userUpdatedAt = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Favorite(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='userFavs', on_delete=CASCADE)
from django.db import models
import re

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['firstName']) < 2:
            error['firstName'] = "First Name must be at least 2 characters"

        if len(form['lastName']) < 2:
            error['lastName'] = "Last Name must be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Format'

        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email addres is already in use'

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] ='Sorry that username has been taken please chose a different one'

        if len(form['password']) < 5:
            errors['password'] = 'Password must be at least 5 characters long'
        
        if form['password'] != form['confirm']:
            errors['password'] = 'Password do not match'

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    objects = UserManager()

class Note(models.Model):
    noteTitle = models.CharField(max_length=45)
    noteText = models.CharField(max_length=300)
    user = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)

class Document(models.Model):
    img = models.ImageField(upload_to='images', default='default.jpg')
    imgName = models.CharField(max_length=255)

class Task(models.Model):
    task = models.CharField(max_length=255)
    desc = models.TextField()
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Student(models.Model):
    sname = models.CharField(max_length=50)
    semail = models.EmailField(max_length=35)
    saddr = models.CharField(max_length=125)


    def __str__(self):
        return self.sname


    def get_absolute_url(self):
        return reverse('stud-create')

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg',upload_to='profile_pics.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'




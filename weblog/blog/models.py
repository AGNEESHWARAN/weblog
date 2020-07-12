from django.db import models

# Create your models here

class User(models.Model):
    username=models.CharField(unique=True,max_length=25)
    password=models.CharField(unique=False,max_length=100)

    def __str__(self):
        return(self.username)

class Blog(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.CharField(unique=False,max_length=1000)
    def __str__(self):
        return(self.username.username)

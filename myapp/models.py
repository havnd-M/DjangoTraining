
from django.db import models
from datetime import datetime

# Create your models here.


"""class Client(models.Model):
    client_name = models.CharField(
        max_length=255, help_text='enter your name', null=True)

    def __str__(self):
        return self.client_name
"""


class Student(models.Model):
    choss = [('male', 'male'), ('female', 'female'), ('other', 'other')]

    #name = models.ForeignKey(Client, on_delete=models.PROTECT, null=True)
    name = models.CharField(
        max_length=255, help_text='enter your name', null=True)

    age = models.IntegerField(
        max_length=50, help_text='Enter your age', null=True)

    email = models.EmailField(max_length=255, unique=True,
                              help_text='enter your email address', null=True,
                              error_messages={'unique': 'dont fuck with me dud enter valid email'})

    gender = models.CharField(max_length=10, null=True,
                              help_text='Enter your gender', choices=choss)

    time = models.DateTimeField(default=datetime.now)

    file = models.FileField(upload_to='myapp/uploads', null=True)

    image = models.ImageField(upload_to='myapp/uploads', null=True)

    class Meta:
        verbose_name = 'Person'
        db_table = 'person_upload'

    def __str__(self):
        return self.name

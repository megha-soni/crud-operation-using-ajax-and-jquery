from django.db import models


# made an User model with 3 fields included name,email,password

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
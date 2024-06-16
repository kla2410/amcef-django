from django.db import models


class user_details(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

# test if return can be  str and int
    def user_details(self):
        return self

class user_content(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100) 

# Create your models here.

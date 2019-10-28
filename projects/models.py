from django.db import models



class Project(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    techology   = models.CharField(max_length=100)
    image       = models.FilePathField('/img')

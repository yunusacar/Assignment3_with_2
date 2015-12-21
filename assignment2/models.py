from __future__ import unicode_literals

from django.db import models

# Create your models here.

class teacher(models.Model):
    fn=models.CharField(max_length=37)
    ls=models.CharField(max_length=57)
    od=models.CharField(max_length=100)
    pn=models.CharField(max_length=15)
    email=models.EmailField()
    def __unicode__(self):
        return self.ls

class course(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=11)
    croom=models.CharField(max_length=10)
    time=models.DateTimeField()
    tc=models.ForeignKey(teacher)
    def __unicode__(self):
        return self.name

class student(models.Model):
    fn=models.CharField(max_length=37)
    ls=models.CharField(max_length=57)
    crs=models.ManyToManyField(course)
    email=models.EmailField()
    def __unicode__(self):
        return self.crs


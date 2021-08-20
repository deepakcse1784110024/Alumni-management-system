from django.db import models
from datetime import date
# Create your models here.

class Alumni(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=20)
    rollno=models.BigIntegerField()
    branch=models.CharField(max_length=100)
    batch_year=models.TextField()
    address=models.TextField()
    occupation=models.TextField()
    company=models.TextField()
    job_title=models.TextField()
    job_location=models.TextField()
    package=models.BigIntegerField()
    skills=models.TextField()
    password=models.CharField(max_length=20)
    objects=models.Manager()
    def __str__(self):
        return self.name

class Blog(models.Model):
    user_id=models.ForeignKey(Alumni,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    title=models.TextField()
    content=models.TextField()
    link=models.TextField()
    img=models.ImageField(upload_to='images/')
    objects=models.Manager()
    def __str__(self):
        return self.title

class Comment(models.Model):
    
    message=models.TextField('Message')
    date_comment = models.DateField(default=date.today)
    user_id= models.ForeignKey(Alumni,on_delete=models.CASCADE)
    post_id= models.ForeignKey(Blog,on_delete=models.CASCADE)

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=20)
    rollno=models.IntegerField(primary_key=True)
    branch=models.CharField(max_length=100)
    batch_year=models.TextField()
    address=models.TextField()
    skills=models.TextField()
    password=models.CharField(max_length=20)
    objects=models.Manager()

class News(models.Model):
    title=models.TextField()
    link=models.TextField()
    date_news = models.DateField(default=date.today)

from home.models import Alumni

from django.db import models

# Create your models here.
class Post(models.Model):
    user_id=models.ForeignKey(Alumni,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    title=models.TextField()
    content=models.TextField()
    link=models.TextField()
    img=models.ImageField(upload_to='images/')
    objects=models.Manager()
    def __str__(self):
        return self.name

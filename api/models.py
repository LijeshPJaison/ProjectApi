from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()

class Post(models.Model):
    images = models.ManyToManyField('Image')
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked = models.BooleanField()

class User(models.Model):
    username = models.CharField(max_length=255)
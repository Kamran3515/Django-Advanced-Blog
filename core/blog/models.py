from django.db import models
from django.contrib.auth import get_user_model

#getting user model object
User = get_user_model()

# Create your models here.
class Post(models.Model):
    """
    this model for posts in blog app
    """

    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    status = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):

    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
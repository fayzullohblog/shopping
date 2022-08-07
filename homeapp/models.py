from secrets import choice
from django.db import models
from accountapp.models import UserModel
# from colorfield.fields import ColorField
# Create your models here.
class ProductModel(models.Model):
    title=models.CharField(max_length=50)
    category=models.ForeignKey('CategoryModel',on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='ProductModel_Image')
    price=models.CharField(max_length=15)
    create_date=models.DateTimeField(auto_now=True)
    newprice=models.CharField(max_length=15)
    product_count=models.PositiveIntegerField(default=0)
    discount=models.PositiveIntegerField(default=0)
    

class ColorModel(models.Model):
    name=models.CharField(max_length=20)
    code=models.CharField(max_length=20)
    def __str__(self):
        return self.title
    


    def __str__(self):
        return self.title
class PostModel(models.Model):
    owner=models.ForeignKey(UserModel,related_name='postmodels',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    body=models.TextField()
    image=models.ImageField(upload_to='PostModel_Image')
    create_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    body=models.TextField()
    owner=models.ForeignKey(UserModel,related_name='commentmodels',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='CommentModel_Image')
    create_date=models.DateTimeField(auto_now=True)
    update_date=models.DateTimeField(auto_now_add=True)
    reply=models.TextField()

    def __str__(self):
        return self.body


class LikeModel(models.Model):
    owner=models.ForeignKey(UserModel,related_name='likemodels',on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.owner

class CategoryModel(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    image=models.ImageField(upload_to='CategoryModel_Image')


    def __str__(self):
        return self.title







  





    



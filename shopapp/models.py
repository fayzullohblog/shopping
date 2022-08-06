from django.db import models
from accountapp.models import UserModel
from homeapp.models import CategoryModel, ProductModel
# Create your models here.
class BannerListModel(models.Model):
    imagebackground=models.ImageField(upload_to='BannerModel_Image')
    imageproduct=models.ImageField(upload_to='ProductModel_Image')
    title=models.CharField(max_length=50)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class WidListModel(models.Model):
    owner=models.ForeignKey(UserModel,related_name='widlistmodels',on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(ProductModel,on_delete=models.SET_NULL,null=True)



class BrandModel(models.Model):
    image=models.ImageField(upload_to='BrandModel_Image')
    title=models.CharField(max_length=50)
    body=models.TextField()

    def __str__(self):
        return self.title

class ImageModel(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='ImageModel_Image')
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class FeedBackModel(models.Model):
    owner=models.ForeignKey(UserModel,related_name='feedbackmodels',on_delete=models.SET_NULL,null=True)
    body=models.TextField()
    
    def __str__(self):
        return self.body

class InformationModel(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.SET_NULL,null=True)
    weight=models.IntegerField(default=0)
    size=models.CharField(max_length=10)
    title=models.CharField(max_length=150)

    def __str__(self):
        return self.title

class CartModel(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='CartModelImage')
    price=models.CharField(max_length=15)
    cart_count=models.PositiveIntegerField(default=0)
    owner=models.CharField(max_length=50,null=True,blank=True)
    create_date=models.DateTimeField(auto_now=True)
   
  
    def __str__(self):
        return self.title


class CartItimModel(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.SET_NULL,null=True)
    cart=models.ForeignKey(CartModel,on_delete=models.SET_NULL,null=True)
    count=models.IntegerField()
    total=models.IntegerField()
    order_time=models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.total


class AdvertisModel(models.Model):
    image=models.ImageField(upload_to='AdvertisModel_Image')
    title=models.CharField(max_length=150)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    








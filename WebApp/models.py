from django.db import models

# Create your models here.

class ContactDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(null=True,blank=True)
    Message = models.TextField(null=True,blank=True)

class UserDb(models.Model):
    Username =models.CharField(max_length=100,null=True,blank=True)
    Email_ID =models.EmailField(max_length=100,null=True,blank=True)
    Password =models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    Cart_Username =models.CharField(max_length=100,null=True,blank=True)
    Cart_ProductName =models.CharField(max_length=100,null=True,blank=True)
    Cart_Quantity =models.IntegerField(null=True,blank=True)
    Cart_Price = models.FloatField(null=True,blank=True)
    Cart_TotalPrice = models.FloatField(null=True,blank=True)
    Cart_ProductImage = models.ImageField(upload_to="Cart_Image",null=True,blank=True)

class  OrderDb(models.Model):
    First_Name = models.CharField(max_length=100,null=True,blank=True)
    Last_Name = models.CharField(max_length=100,null=True,blank=True)
    Email_ID = models.EmailField(max_length=100,null=True,blank=True)
    Place =models.CharField(max_length=100,null=True,blank=True)
    Address =models.CharField(max_length=100,null=True,blank=True)
    Mobile =models.CharField(max_length=100,null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    Pincode = models.CharField(max_length=100,null=True,blank=True)
    TotalPrice = models.FloatField(null=True,blank=True)

class BlogDb(models.Model):
    Blog_Title = models.CharField(max_length=100,null=True,blank=True)
    Blog_Description = models.TextField(null=True,blank=True)
    Blog_Image = models.ImageField(upload_to="Blog_Image",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # This field will automatically update every time the object is saved
    updated_at = models.DateTimeField(auto_now=True)
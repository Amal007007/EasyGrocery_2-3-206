from django.db import models
from unicodedata import category


# Create your models here.
class CategoryDb(models.Model):
    CategoryName = models.CharField(max_length=100, unique=True)
    CategoryDescription = models.TextField()
    CategoryImage = models.ImageField(upload_to="categories" )


    def __str__(self):
        return self.CategoryName

class ProductDb(models.Model):
    Category_Name = models.CharField(max_length=100)
    Product_Name = models.CharField(max_length=100,unique=True)
    Product_Price = models.FloatField()
    Product_Description = models.TextField()
    Product_Image = models.ImageField(upload_to="products")
    def __str__(self):
        return self.Product_Name


class ServiceDb(models.Model):
    ServiceName = models.CharField(max_length=100)
    ServiceDescription = models.TextField()
    ServiceImage = models.ImageField(upload_to="services")
    def __str__(self):
        return self.ServiceName


from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=8, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=3)
    cost = models.DecimalField(max_digits=12, decimal_places=3)
    stock = models.IntegerField()


class Kit(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=8, unique=True)
    products = models.ManyToManyField(Product, through='KitRelation')


class KitRelation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    amount = models.IntegerField()
    discount = models.DecimalField(max_digits=6, decimal_places=3)



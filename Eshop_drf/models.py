
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(max_length=15)
    quantity = models.IntegerField()
    exp_date = models.DateField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    quantity = models.IntegerField()
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchase')
    vendor_id = models.OneToOneField(Vendor, on_delete=models.CASCADE)

    @property
    def total_price(self):
        price = self.quantity * self.product.price
        return price


class Sales(models.Model):
    quantity = models.IntegerField()
    date = models.DateField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.FloatField()

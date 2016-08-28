# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.name


class Jobtype(models.Model):
    job = models.CharField(max_length=30)

    class Meta:
        db_table = 'JobType'

    def __str__(self):
        return self.job


class Order(models.Model):
    product = models.ForeignKey('Product', models.SET_NULL, null=True)
    ordered_date = models.DateField(auto_now_add=True)
    quantity_ordered = models.IntegerField()
    staff = models.ForeignKey('Staff', models.SET_NULL, null=True)
    status = models.ForeignKey('Status', models.SET_NULL, null=True)

    class Meta:
        db_table = 'Order'

    def __str__(self):
        return self.product.name


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=40)
    stock = models.IntegerField(default=0)
    cost_price = models.FloatField()
    sell_price = models.FloatField()
    category = models.ForeignKey(Category, models.SET_NULL, null=True)
    supplier = models.ForeignKey('Supplier', models.SET_NULL, null=True)
    mfd_date = models.DateField()
    exp_date = models.DateField()
    rack = models.ForeignKey('Rack', models.SET_NULL, null=True)

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name


class Rack(models.Model):
    col_num = models.IntegerField()

    class Meta:
        db_table = 'Rack'

    def __str__(self):
        return str(self.col_num)


class Staff(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    name = models.CharField(max_length=40)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    jobtype = models.ForeignKey(Jobtype, models.SET_NULL, null=True)
    address = models.CharField(max_length=40)

    class Meta:
        db_table = 'Staff'

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'Supplier'

    def __str__(self):
        return self.name


class Bill(models.Model):
    staff = models.ForeignKey(Staff, models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'bill'

    def __str__(self):
        return str(self.pk)

    def total_price(self):
        total = 0.0
        for sale in self.product_sale_set.all():
            total += sale.product.sell_price * sale.quantity
        return total


class ProductSale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    bill = models.ForeignKey(Bill, related_name='product_sale_set', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'bill_detail'

    def __str__(self):
        return str(self.pk)


class Status(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.name

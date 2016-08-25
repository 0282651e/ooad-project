# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

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
        return self.name


class Order(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING)
    ordered_date = models.DateField()
    quantity_ordered = models.IntegerField()
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    status = models.ForeignKey('Status', models.DO_NOTHING)

    class Meta:

        db_table = 'Order'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=40)
    stock = models.IntegerField()
    cost_price = models.FloatField()
    sell_price = models.FloatField()
    category = models.ForeignKey(Category, models.DO_NOTHING)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING)
    mfd_date = models.DateField()
    exp_date = models.DateField()
    rack = models.ForeignKey('Rack', models.DO_NOTHING)

    class Meta:

        db_table = 'Product'

    def __str__(self):
        return self.name


class Rack(models.Model):
    col_num = models.IntegerField()

    class Meta:

        db_table = 'Rack'


class Staff(models.Model):
    name = models.CharField(max_length=40)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    jobtype = models.ForeignKey(Jobtype, models.DO_NOTHING)
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
    staff = models.ForeignKey(Staff, models.DO_NOTHING)
    total_amount = models.FloatField()
    created_at = models.DateTimeField()

    class Meta:

        db_table = 'bill'


class BillDetail(models.Model):
    product_id = models.CharField(max_length=5)
    bill = models.ForeignKey(Bill)
    quantity_bought = models.IntegerField()

    class Meta:

        db_table = 'bill_detail'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)

    class Meta:

        db_table = 'status'

    def __str__(self):
        return self.name

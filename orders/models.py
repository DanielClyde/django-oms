from django.db import models

# Create your models here.
class State(models.Model):
  code = models.CharField(primary_key=True, max_length=2)
  saleTax = models.FloatField()
  def __str__(self):
    return self.code

class Customer(models.Model):
  _id = models.CharField(primary_key=True, max_length=20)
  name = models.CharField(max_length=20)
  def __str__(self):
    return self._id + ': ' + self.name

class Part(models.Model):
  _id = models.CharField(primary_key=True, max_length=20)
  unitCost = models.IntegerField(default=0)
  name = models.CharField(max_length=50)
  imgName = models.CharField(max_length=50, default='')
  obsolete = models.BooleanField(default=False)
  def __str__(self):
    return self._id + ': ' + self.name

class Order(models.Model):
  _id = models.CharField(primary_key=True, max_length=20)
  customerNumber = models.ForeignKey(Customer, on_delete=models.PROTECT)
  shippingTotal = models.IntegerField(default=0)

class Item(models.Model):
  _id = models.AutoField(primary_key=True)
  sequenceNumber = models.IntegerField()
  orderNumber = models.ForeignKey(Order, on_delete=models.CASCADE)
  partNumber = models.ForeignKey(Part, on_delete=models.PROTECT)
  quantity = models.IntegerField()

class CustomerState(models.Model):
  _id = models.AutoField(primary_key=True)
  customerNumber = models.ForeignKey(Customer, on_delete=models.PROTECT)
  state = models.ForeignKey(State, to_field='code', on_delete=models.PROTECT)
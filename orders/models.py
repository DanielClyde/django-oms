from django.db import models


# Create your models here.

class Customer(models.Model):
    _id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True)

    def __str__(self):
        return str(self._id) + ': ' + str(self.name)


class Part(models.Model):
    _id = models.CharField(primary_key=True, max_length=20)
    unitCost = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    obsolete = models.BooleanField(default=False)

    def __str__(self):
        return str(self._id) + ': ' + str(self.name)


class Order(models.Model):
    _id = models.CharField(primary_key=True, max_length=20)
    customerNumber = models.ForeignKey(Customer, on_delete=models.PROTECT)
    shippingTotal = models.IntegerField(default=0)

    def __str__(self):
        return str(self._id) + ': ' + str(self.customerNumber)


class Item(models.Model):
    _id = models.AutoField(primary_key=True)
    sequenceNumber = models.IntegerField()
    orderNumber = models.ForeignKey(Order, on_delete=models.CASCADE)
    partNumber = models.ForeignKey(Part, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self._id) + ': ' + str(self.quantity) + ' x ' + str(self.partNumber) + ' - ' + self.orderNumber



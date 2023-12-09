from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Status(models.Choices):
    INITIAL = "INITIAL"
    PAYMENT = "PAYMENT"
    ACCEPTED = "ACCEPTED"
    CANCELED = "CANCELED"
    DELIVERED = "DELIVERED"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    create_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    total_price = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_discount = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=Status.choices)


class OrderProduct(models.Model):
    product = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)


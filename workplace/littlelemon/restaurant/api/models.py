from django.db import models

# Create your models here.
class Booking(models.Model):
  name = models.CharField(max_length=255)
  no_guest = models.IntegerField()
  booking_date = models.DateTimeField()

  def __str__(self):
    return f"{self.name} {self.no_guest} {self.booking_date}"
  
class Menu(models.Model):
  title = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  inventory = models.IntegerField()

  def __str__(self):
    return f"{self.title} {self.price} {self.inventory}"
  
class User(models.Model):
  url = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  email = models.CharField(max_length= 255)
  groups = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.url} {self.username} {self.email} {self.groups}"
  
# class MenuItem(models.Model):
  title = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  inventory = models.IntegerField()

  def __str__(self):
    return f"{self.title} {self.price} {self.inventory}"
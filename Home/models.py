from django.db import models


class CitrusPlant(models.Model):
    picture = models.ImageField(upload_to='citrus_plant_pics/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class BerryPlant(models.Model):
    picture = models.ImageField(upload_to='berry_plant_pics/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class AnnualPlant(models.Model):
    picture = models.ImageField(upload_to='annual_plant_pics/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class PerinnialPlant(models.Model):
    picture = models.ImageField(upload_to='perinnial_plant_pics/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class BiennialPlant(models.Model):
    picture = models.ImageField(upload_to='biennial_plant_pics/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class AirPurifierPlant(models.Model):
    picture = models.ImageField(upload_to='airpurifier_plant_pics/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  
    email = models.EmailField(default='')
    def __str__(self):
        return self.username
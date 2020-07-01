from django.db import models

# Create your models here.
class Product(models.Model):
    title      =models.CharField(max_length=120)
    description=models.TextField(blank=False,null=False)
    price      =models.DecimalField(decimal_places=2,max_digits=100000)
    summary    =models.TextField(default='this is cool')

class Sales(models.Model):
    sales =models.TextField()


class Shree(models.Model):
    pregnancy = models.FloatField(null=False)
    glucose = models.FloatField(null=False)
    blood_pressure = models.FloatField(null=False)
    skin_thickness = models.FloatField(null=False)
    insulin = models.FloatField(null=False)
    bmi = models.FloatField(null=False)
    diabetes_pedigree_fucntion = models.FloatField(null=False)
    age = models.FloatField(null=False)
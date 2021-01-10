from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50,primary_key=True,unique=True)
    password = models.CharField(max_length=50)
class Datasets(models.Model):
    dataset_name = models.CharField(max_length=50)
    user_name = models.ForeignKey(User,on_delete=models.PROTECT)
class WeatherDataset(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.PROTECT)
    dataset_name = models.ForeignKey(Datasets,on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    temp = models.CharField(max_length=50)
    feels_like = models.CharField(max_length=50)
    temp_min = models.CharField(max_length=50)
    pressure = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    visibility = models.CharField(max_length=50)
    iconUrl = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
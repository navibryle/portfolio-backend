from django.db import models
import datetime
from django.views.generic.dates import DateMixin
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
    temp_max = models.CharField(max_length=50)
    pressure = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    visibility = models.CharField(max_length=50)
    iconUrl = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

#F=================================



# Create your models here.
class UseName(models.Model):
    user_Name = models.CharField(max_length=60, unique=True)
    pas = models.CharField(max_length=50)

    def __str__(self):
        return self.user_Name + " " + self.pas

class AccessData(models.Model):
    user = models.CharField(max_length=60)
    item = models.CharField(max_length=75)
    date = models.DateField()
    endDate = models.DateField(True, default=0)

    def __str__(self):
        return str(self.date) + " " + self.item + " " + self.user + " " + str(self.endDate)

class DoneData(models.Model):
    user = models.CharField(max_length=60)
    item = models.CharField(max_length=75)
    dateEnded = models.DateField()

    def __str__(self):
        return str(self.dateEnded) + " " + self.item + " " + self.user
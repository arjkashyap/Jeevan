from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import date

class Emarket(models.Model):      # These are our database files for the Shop
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    city_location = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    logo = models.FileField()
    verify = models.BooleanField(default = False)
    latt = models.FloatField(default = 30)
    lonn = models.FloatField(default = 25)

    def get_absolute_url(self):
        return reverse('main:added')

    def __str__(self):                  # Displays the following  when a query is made
      return self.name + '-' + self.owner 

class Details(models.Model):
    shop = models.ForeignKey(Emarket, on_delete = models.CASCADE, related_name='banana_pudding')    
    shop_name = models.CharField(max_length = 30)
    shop_img = models.FileField()
    shop_contact = models.CharField(max_length = 600, default = "Enter all means to contact.")
    shop_details = models.TextField(max_length= 2500)
    shop_address = models.TextField(max_length = 600, default = "Address")
    shop_doc = models.FileField()

    def __str__(self):
        return self.shop_name 

class Plantation(models.Model):
    name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 40)
    date = models.CharField(max_length = 40)
    contact = models.CharField(max_length = 40)
    description = models.TextField(max_length= 2500)
 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:join')
    

class Join(models.Model):
    name = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 100, default = "Enter phone number.")
    email = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:added')

class Discover(models.Model):
    image = models.FileField()
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 20)
    description = models.TextField(max_length = 100)


    def __str__(self):
        return self.name

class DiscDetails(models.Model):
    innov = models.ForeignKey(Discover, on_delete = models.CASCADE, related_name='banana_pudding') 
    heading = models.CharField(max_length = 20)
    sub = models.CharField(max_length = 25)   
    passage = models.TextField(max_length = 2500)
    video = models.CharField(max_length = 100)

    def __str__(self):
        return self.heading
    
    def get_absolute_url(self):
        return reverse('main:added')
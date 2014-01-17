from django.db import models

# Create your models here.
class Contact(models.Model):
   # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1800)
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=1500)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=90)
    pin_code = models.CharField(max_length=10 )
    phone_no = models.CharField(max_length=50)
    
    

class DelegateFees(models.Model):
   # id = models.IntegerField(primary_key=True)
    reg_type = models.CharField(max_length=300)
    fees = models.CharField(max_length=300)
    
class Events(models.Model):
   # id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=90)
    title = models.CharField(max_length=90)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    detail = models.CharField(max_length=2500)
    #tragetaudience = models.CharField(max_length=1800)
    subtitle = models.CharField(max_length=90)

class Program(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)   
    date = models.DateTimeField()
    venue = models.CharField(max_length=50, blank=True)
    by = models.CharField(max_length=150)
           

class Participants(models.Model):
   # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1500)
    website = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    logo = models.ImageField(upload_to = 'files')

class Schedule(models.Model):
   # id = models.IntegerField(primary_key=True)
    day = models.CharField(max_length=450)
    title = models.CharField(max_length=900)
    description = models.CharField(max_length=45000)
    room_no = models.IntegerField()
    start_time = models.DateField()
   # end_time = models.DateTimeField()
    

class Sponsorship(models.Model):
  #  id = models.IntegerField(primary_key=True)
    packages = models.CharField(max_length=900)
    amount = models.CharField(max_length=900)
    free_delegates = models.IntegerField()
    exhibition_space = models.CharField(max_length=180)
    dinner_spaces = models.IntegerField()
    
class Audience(models.Model):
    audience = models.CharField(max_length=200)

class Diamond(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=5000)
    link = models.CharField(max_length=50)
    logo = models.ImageField(upload_to = 'files')

class Gold(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=5000)
    link = models.CharField(max_length=50)
    logo = models.ImageField(upload_to = 'files')              

class Silver(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=5000)    
    link = models.CharField(max_length=50)
    logo = models.ImageField(upload_to = 'files')          

class Variables(models.Model):
     sitelogo = models.ImageField(upload_to = 'files')
     sitename = models.CharField(max_length=25)

class Travel(models.Model):
    name = models.CharField(max_length=50)
    subject =  models.CharField(max_length=2000)
    contact =  models.CharField(max_length=500)


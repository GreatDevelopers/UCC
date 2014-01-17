from django.db import models
from userprofile.models import BaseProfile
from django.utils.translation import ugettext as _
from django.conf import settings
import datetime

STATES_CHOICES = (
    ('Andhra Pradesh', _('Andhra Pradesh')),
    ('Arunachal Pradesh', _('Arunachal Pradesh')),
    ('Assam', _('Assam')),
    ('Bihar', _('Bihar')),
    ('Chhattisgarh', _('Chhattisgarh')),
    ('Chandigarh',_('chandigarh')),
    ('Delhi', _('Delhi')),
    ('Goa', _('Goa')),
    ('Gujarat', _('Gujarat')),
    ('Haryana', _('Haryana')),
    ('Himachal Pradesh', _('Himachal Pradesh')),
    ('Jammu and Kashmir', _('Jammu and Kashmir')),
    ('Jharkhand', _('Jharkhand')),
    ('Karnataka', _('Karnataka')),
    ('Kerala', _('Kerala')),
    ('Madhya Pradesh', _('Madhya Pradesh')),
    ('Maharashtra', _('Maharashtra')),
    ('Manipur', _('Manipur')),
    ('Meghalaya', _('Meghalaya')),
    ('Mizoram', _('Mizoram')),
    ('Nagaland', _('Nagaland')),
    ('Orissa', _('Orissa')),
    ('Punjab', _('Punjab')),
    ('Rajasthan', _('Rajasthan')),
    ('Sikkim', _('Sikkim')),
    ('Tamil Nadu', _('Tamil Nadu')),
    ('Tripura', _('Tripura')),
    ('Uttar Pradesh', _('Uttar Pradesh')),
    ('Uttarakhand', _('Uttarakhand')),
    ('West Bengal', _('West Bengal')),
) 

	
GENDER_CHOICES = ( ('F', _('Female')), ('M', _('Male')),)
COUSRE_CHOICES = ( ('B.Tech', _('B.Tech')), ('M.Tech', _('M.Tech')),('MBA', _('MBA')), ('MCA', _('MCA')),)
BRANCH_CHOICES = ( ('Information Technology', _('IT')), ('Computer Science & Engineering', _('CSE')), ('Electrical Engineering', _('EE')), ('Mechanical Engineering', _('ME')), ('Civil Engineering ', _('CE')),('Electronics & Communication Engineering', _('ECE')), ('Production Engineering', _('PE')), )

class Profile(BaseProfile):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255,blank=True )
    lastname = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    course = models.CharField(max_length=15, choices=COUSRE_CHOICES)
    branch = models.CharField(max_length=50,help_text="(only for B.Tech Students)", choices=BRANCH_CHOICES, blank=True)
    class_roll_no = models.IntegerField(null=True)
    photo =models.ImageField(upload_to = 'files' ,help_text="(Only use Passport Size Color photograph(1.5 inch * 2.0 inch) and resolution should be set to 300-600 dpi.)")
    father_name =models.CharField(max_length=100)
    mother_name =models.CharField(max_length=100)
    birthdate = models.DateField(default=datetime.date.today())
    #url = models.URLField(blank=True)
    address_1 =models.CharField(max_length=255, )
    address_2 =models.CharField(max_length=255, blank=True )
    city =models.CharField(max_length=255)
    pin_code = models.IntegerField(null=True)
    state=models.CharField(max_length=30, choices=STATES_CHOICES, default='Punjab')
    email =models.EmailField()
    contact_no =models.CharField(max_length=25)
    comments =models.TextField()
    

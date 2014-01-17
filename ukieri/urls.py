from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from mysite.ukieri.models import *


urlpatterns = patterns('mysite.ukieri.views',
    (r'^$', 'index'),
    (r'^contact/$', 'contact'),
    (r'^sponsorship/$','sponsorship'),
    (r'^events/$','events'),
    (r'^travel/$','travel'),
    (r'^schedule/$','schedule'), 
    (r'^audience/$','audience'),
    (r'^participants/$','participants'),
    (r'^home/$','home'),
#    (r'^footer/$','footer'),
    (r'^sponsors/$','sponsors'),
    (r'^reach/$','reach'),
    (r'^credits/$','credits'),
    (r'^exhibitors/$','exhibitors'), 
    (r'^program/$','program'),
    (r'^header/$','header'), 
)

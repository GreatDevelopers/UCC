from django.conf.urls.defaults import *
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      (r'^admin/', include(admin.site.urls)),
      (r'^polls/', include('mysite.polls.urls')),
      (r'^maths/', include('mysite.maths.urls')),
      (r'^blog/', include('mysite.blog.urls')),
      (r'^contact/', 'mysite.contact.views.contact'),
      (r'^add/', 'mysite.add.views.add'),
      (r'^lug/', 'mysite.lug.views.camp_registration'),
      (r'^add_db/$', 'mysite.add_db.views.add_db'),
      (r'^add_db/result/$', 'mysite.add_db.views.result'),
      (r'^ukieri/', include('mysite.ukieri.urls')),
#      (r'^accounts/', include('registration.urls')),
      (r'^performa/$', 'mysite.performa.views.student'),
      (r'^souvenir/fulldetail/', 'mysite.student.views.fulldetail'),
      (r'^souvenir/detail/', 'mysite.student.views.detail'),
      (r'^souvenir/CE/', 'mysite.student.views.ce'),
      (r'^souvenir/ECE/', 'mysite.student.views.ece'),
      (r'^souvenir/ME/', 'mysite.student.views.me'),
      (r'^souvenir/PE/', 'mysite.student.views.pe'),
      (r'^souvenir/CSE/', 'mysite.student.views.cse'),
      (r'^souvenir/EE/', 'mysite.student.views.ee'),
      (r'^souvenir/IT/', 'mysite.student.views.it'),
      (r'^souvenir/MBA/', 'mysite.student.views.mba'),      
      (r'^$', TemplateView,{ 'template': 'index.html' }, 'index'),
    
)

urlpatterns += patterns('',
    (r'^accounts/', include('userprofile.urls')),
)

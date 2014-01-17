from django.contrib import admin
from mysite.ukieri.models import *

class Contacts(admin.ModelAdmin):
        list_display = ('id', 'name', 'email', 'address', 'country', 'city', 'pin_code', 'phone_no')
        list_filter = ['id']
        search_fields = ['id']

class Audiences(admin.ModelAdmin):
	list_display = ('id', 'audience' )
        list_filter = ['id']
        search_fields = ['id']
class DelegateFee(admin.ModelAdmin):
	list_display = ('id', 'reg_type', 'fees' )
        list_filter = ['id']
        search_fields = ['id']
class Event(admin.ModelAdmin):
	list_display = ('id', 'type', 'title', 'date', 'venue', 'detail' )
        list_filter = ['id']
        search_fields = ['id']
class Programs(admin.ModelAdmin):
	list_display = ('id', 'title','subtitle', 'date', 'venue', 'by' )
        list_filter = ['id']
        search_fields = ['id']
class Participant(admin.ModelAdmin):
	list_display = ('id', 'name', 'website', 'country', 'city', 'logo' )
        list_filter = ['id']
        search_fields = ['id']

class Schedules(admin.ModelAdmin):
	list_display = ('id', 'day', 'title', 'description', 'room_no', 'start_time' )
        list_filter = ['id']
        search_fields = ['id']
class Sponsorships(admin.ModelAdmin):
	list_display = ('id', 'packages', 'amount', 'free_delegates', 'exhibition_space','dinner_spaces' )
        list_filter = ['id']
        search_fields = ['id']

class Diamonds(admin.ModelAdmin):
	list_display = ('id', 'name', 'info','link','logo' )
        list_filter = ['id']
        search_fields = ['id']

class Golds(admin.ModelAdmin):
	list_display = ('id', 'name', 'info', 'link', 'logo' )
        list_filter = ['id']
        search_fields = ['id']

class Silvers(admin.ModelAdmin):
	list_display = ('id', 'name', 'info','link','logo' )
        list_filter = ['id']
        search_fields = ['id']

class Variable(admin.ModelAdmin):
	list_display = ('id', 'sitelogo', 'sitename' )
        list_filter = ['id']
        search_fields = ['id']
class Travels(admin.ModelAdmin):
        list_display = ('id', 'name', 'subject','contact' )
        list_filter = ['id']
        search_fields = ['id']

admin.site.register(Contact, Contacts)
admin.site.register(DelegateFees, DelegateFee)
admin.site.register(Events, Event)
admin.site.register(Sponsorship, Sponsorships)
admin.site.register(Schedule, Schedules)
admin.site.register(Participants, Participant)
admin.site.register(Audience, Audiences)
admin.site.register(Diamond, Diamonds)
admin.site.register(Gold, Golds)
admin.site.register(Silver, Silvers)
admin.site.register(Travel, Travels)
admin.site.register(Variables, Variable)
admin.site.register(Program, Programs)

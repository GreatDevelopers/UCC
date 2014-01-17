from django.contrib import admin
from mysite.student.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date','class_roll_no','course','branch' )
    search_fields = ('class_roll_no',)

admin.site.register(Profile, ProfileAdmin)

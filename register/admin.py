from django.contrib import admin
from register.models import Profile
from register.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['sname','semail','saddr']

admin.site.register(Student,StudentAdmin)

admin.site.register(Profile)
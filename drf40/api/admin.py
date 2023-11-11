from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']
    
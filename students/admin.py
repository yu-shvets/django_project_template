from django.contrib import admin
from .models.students import Student, Group
from .models.exams import Ex

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Ex)
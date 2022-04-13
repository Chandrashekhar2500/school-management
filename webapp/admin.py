from django.contrib import admin
from .models import teachers
from .models import students
# Register your models here.
admin.site.register(teachers)
admin.site.register(students)

from django.contrib import admin
from .models import Student
from .models import IndexText
from .models import About
from .models import AboutSlide
# Register your models here.
admin.site.register(Student)
admin.site.register(IndexText)
admin.site.register(About)
admin.site.register(AboutSlide)
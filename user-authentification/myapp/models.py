from django.db import models

# Create your models here.
class Student(models.Model):
    title=models.CharField(max_length=50)
    detail=models.CharField(max_length=500)


# class Image(models.Model):
   
   

class IndexText(models.Model):
    title=models.CharField(max_length=50)
    blog1=models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/%y")   
    caption=models.CharField(max_length=50)
    

class About(models.Model):
    title=models.CharField(max_length=50)
    summary=models.CharField(max_length=150)
    text=models.CharField(max_length=100)

class AboutSlide(models.Model):
    topic=models.CharField(max_length=100)
    discription=models.CharField(max_length=200)
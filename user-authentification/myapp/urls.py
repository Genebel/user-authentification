from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signIn', views.signIn, name='signIn'),
    path('signUp', views.signUp, name='signUp'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('services', views.services, name='services'),
    path('team', views.team, name='team'),
    path('blog', views.blog, name='blog'),
    path('post/<str:pk>', views.post, name='post'),
    path('counter', views.counter, name='counter')
    
]

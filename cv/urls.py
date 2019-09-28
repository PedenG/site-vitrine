from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('accueil', views.mainpage, name='accueil'),
    path('about', views.about, name='about'),
    path('contact', views.send_email, name='contact'),
]

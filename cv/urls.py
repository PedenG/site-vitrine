from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('contact', views.contact, name='contact'),
    path('cv', views.cv, name='cv'),
    path('blog', views.blog, name='blog'),
]

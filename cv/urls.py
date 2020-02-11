from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('about', views.about, name='about'),
    path('contact', views.send_email, name='contact'),
    path('robots.txt', TemplateView.as_view(template_name="cv/robots.txt", content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name="cv/sitemap.xml", content_type='application/xml')),
    path('404.html', TemplateView.as_view(template_name="404.html", content_type='text/html'))
]

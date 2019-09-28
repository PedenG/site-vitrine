from django.urls import path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap
from . import views


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('accueil', views.mainpage, name='accueil'),
    path('about', views.about, name='about'),
    path('contact', views.send_email, name='contact'),
    path('robots.txt', TemplateView.as_view(template_name="cv/robots.txt", content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap')
]

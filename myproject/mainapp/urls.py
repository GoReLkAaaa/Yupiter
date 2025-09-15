from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/ru/', views.contact, name='contact'),
    path('about/ru/', views.about, name='about'),
    path('products/ru/', views.products, name='products'),


    path('yupiter/uz/', views.yupiter_uz, name='yupiter_uz'),
    path('contact/uz/', views.contact_uz, name='contact_uz'),
    path('about/uz/', views.about_uz, name='about_uz'),
    path('products/uz/', views.products_uz, name='products_uz'),
]
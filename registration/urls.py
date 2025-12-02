from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_company, name='register'),
    path('success/', views.success, name='success'),
]

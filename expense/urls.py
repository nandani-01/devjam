from atexit import register
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register',views.register, name = 'register'),
    path('next/', views.next_page, name='next'),
    path('first/', views.first, name='first'),
    path('login', views.loginpage, name='login')
]

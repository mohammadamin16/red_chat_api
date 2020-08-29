from django.urls import path
from accounts import views

urlpatterns = [
    path('welcome', views.welcome),
    path('signup', views.signup),
    path('login', views.login),
    path('get_teachers', views.get_teacher),
    path('is_username_valid', views.is_username_valid),
]

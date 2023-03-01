from django.urls import path
from . import views

urlpatterns = [

    path('inscription/', views.inscription_page, name='inscription'),
    path('login/', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),

    ]
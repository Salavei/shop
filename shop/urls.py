from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.main_page),
    path('login/', views.login_page),
    path('register/', views.register_page),
    path('castom/', views.catsom_page),
    path('logout/', views.logout_user),
    path('profile/', views.profile),
]
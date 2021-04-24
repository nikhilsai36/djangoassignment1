from .views import *
from django.urls import path


urlpatterns = [
    path('details/', details),
    path('create/', create),
    path('register/', register),
    path('edit/<int:id>', edit),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete1),
    path('login/', us_login),
    path('logout/', us_logout),
    path('info/', sqlquaries),
    path('home/', home),


]
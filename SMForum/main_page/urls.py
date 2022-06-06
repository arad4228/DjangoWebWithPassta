from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[
    path('logout/', auth_views.LogoutView.as_view()),
    path('', views.landing),
]
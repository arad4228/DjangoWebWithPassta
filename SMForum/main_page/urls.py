from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[
    path('logout/', auth_views.LogoutView.as_view()),
    path('about_me/', views.about_me),
    path('update_user/', views.update_user),
    path('', views.landing),
]
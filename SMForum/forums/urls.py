from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),

    path('category/<str:slug>/', views.show_category_posts),
    path('tag/<str:slug>/', views.show_tag_posts),
    path('status/<str:slug>', views.show_status_posts),

    path('post/<int:pk>/', views.PostDetail.as_view()),
    path('post/<int:pk>/addComment/', views.add_Comment),

    path('post/', views.PostList.as_view())

]
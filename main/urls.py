from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_details/<slug:slug>/', views.post_details, name='post_details'),
    path('create_post/', views.create_post, name='create_post'),

]

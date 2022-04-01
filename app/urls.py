from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user_profile/<int:user_id>/',
         views.user_profile, name='user_profile'),
    path('deleteProfile/', views.deleteProfile, name='deleteProfile'),
]

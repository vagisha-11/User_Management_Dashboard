from django.urls import path
from . import views
from .views import home


urlpatterns = [
    path('', home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('users/add/', views.add_user, name='add_user'),
   
    path('users/edit/', views.edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user')
]
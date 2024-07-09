from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
    path('farm/<int:farm_id>/', views.farm_detail, name='farm_detail'),
    path('add_farm/', views.add_farm, name='add_farm'),
    path('farm/<int:farm_id>/edit/', views.edit_farm, name='edit_farm'),
    path('farm/<int:farm_id>/delete/', views.delete_farm, name='delete_farm'),
    path('farm/<int:farm_id>/add_horse/', views.add_horse, name='add_horse'),
    path('farm/<int:farm_id>/horse/<int:horse_id>/edit/', views.edit_horse, name='edit_horse'),
    path('farm/<int:farm_id>/horse/<int:horse_id>/delete/', views.delete_horse, name='delete_horse'),
    path('add_user/', views.add_user, name='add_user'),
]

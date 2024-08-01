from django.urls import path
from .views import views

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
    path('farm/<int:farm_id>/add_employee/', views.add_employee, name='add_employee'),
    path('farm/<int:farm_id>/employee/<int:employee_id>/edit/', views.edit_employee, name='edit_employee'),
    path('farm/<int:farm_id>/employee/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
    path('farm/<int:farm_id>/add_trainingsession/', views.add_trainingsession, name='add_trainingsession'),
    path('farm/<int:farm_id>/trainingsession/<int:trainingsession_id>/edit/', views.edit_trainingsession, name='edit_trainingsession'),
    path('farm/<int:farm_id>/trainingsession/<int:trainingsession_id>/delete/', views.delete_trainingsession, name='delete_trainingsession'),
    path('add_user/', views.add_user, name='add_user'),
]

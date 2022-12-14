from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedules_list, name='schedules_list'),
    path('schedule', views.schedule, name='schedule'),
    path('check_available_classrooms', views.check_available_classrooms, name='check_available_classrooms'),
    path('check_available_classrooms_form', views.check_available_classrooms_form, name='check_available_classrooms_form'),
    path('check_classroom_availability', views.check_classroom_availability, name='check_classroom_availability'),
    path('update_schedules', views.update_schedules, name='update_schedules'),
]

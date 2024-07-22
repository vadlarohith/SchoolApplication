from django.urls import path
from . import views

urlpatterns = [
    path('TeacherLogin', views.TeacherLogin, name='TeacherLogin'),
    path('UpdateTeacherDetails', views.UpdateDetails, name="UpdateTeacherDetails"),
    path('Attendence', views.Attendence, name='Attendence'),
]

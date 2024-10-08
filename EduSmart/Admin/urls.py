from django.urls import path
from . import views

urlpatterns = [
    path("",views.test, name="test"),
    path('admin-login/', views.AdminLogin, name='admin_login'),
    path('student-registration/', views.StudentRegistration, name='student_registration'),
    path('TeacherRegistraion', views.TeacherRegistration, name='TeacherRegistration'),
    path('UploadImage', views.UploadImage, name='UploadImage'),
    path('ImageList', views.ImageList, name='ImageList'),
    path('TimeTable', views.TimeTable, name='TimeTable'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('delete_subject/', views.delete_subject, name='delete_subject'),
    path('UpdateFeeDetails', views.UpdateFeeDetails, name='UpdateFeeDetails'),
    path('UpdateFee', views.UpdateFees, name='UpdateFee'),
    path('get-transaction-history/<str:student_roll_no>', views.TransactionHistory, name='get_transaction_history'),
    path('UpdateExamType', views.ExamType, name='UpdateExamType'),
    path('ExamMarksAccess', views.ExamMarksAccess, name='ExamMarksAccess'),
    path('DeleteTimetable', views.DeleteTimetable, name='DeleteTimetable'),
    path('TeacherTimetable', views.TeacherTimetable, name='UpdateTeacherTimetable'),
    path('DeleteTeacherTimetable', views.DeleteTeacherTimetable, name='DeleteTeacherTimetable')
]
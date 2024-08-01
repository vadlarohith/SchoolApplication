from django.contrib import admin
from . import models

admin.site.register(models.Admin)

class StudentPreview(admin.ModelAdmin):
    list_display = ('FullName','Class','RollNo','MobileNo')

admin.site.register(models.Student, StudentPreview)

class TeacherPreview(admin.ModelAdmin):
    list_display = ('FullName','TeacherID','ClassTeacher')

admin.site.register(models.Teacher, TeacherPreview)

admin.site.register(models.Posters)

admin.site.register(models.TimeTable)

class AttendencePreview(admin.ModelAdmin):
    list_display = ('RegNo','Month','Attendence')

admin.site.register(models.Attendence, AttendencePreview)

admin.site.register(models.Class)

admin.site.register(models.Subject)

class UpdateFeePreview(admin.ModelAdmin):
    list_display = ('Class','Fee')

admin.site.register(models.UpdateFee, UpdateFeePreview)

class AttendenceDetailsPreview(admin.ModelAdmin):
    list_display = ('RegNo','AttendenceDate','Attendence')

admin.site.register(models.AttendenceDetails, AttendenceDetailsPreview)

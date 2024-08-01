from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.hashers import check_password
from Admin import models
from . import models as Smodels

def StudentLogin(request):
    StudentPage = loader.get_template("StudentLogin.html")
    HomePage = loader.get_template("home.html")
    Data = models.Student.objects.all().values()
    if request.method == 'POST':
        FullName = request.POST.get('StudentUserName')
        Password = request.POST.get('StudentPassword')
        SRegNo = request.POST.get('StudentRollNo')
 
        try:
            user = models.Student.objects.filter(FullName = FullName, Password = Password).first()
            if user:
                image = models.Posters.objects.all().values()
                data = models.Student.objects.all()
                Class = user.Class
                TimeTable = models.TimeTable.objects.filter(Class = Class).first()
                
                Subjects = models.Subject.objects.filter(Class = user.Class)
                FeeDetails = Smodels.FeeDetails.objects.filter(StudentRollNo = user.RollNo, StudentName = user.FullName).first()
                context = {
                    'Student': FullName,
                    'image' : image,
                    'data' : {
                        'FullName': user.FullName,
                        'RollNo' : user.RollNo,
                        'MobileNo': user.MobileNo,
                        'Password': user.Password,
                        'Class': user.Class
                    },
                    'TimeTable' : TimeTable.Image,
                    
                    'Subjects' : Subjects,
                    'FeeDetails' : FeeDetails
                }
                return HttpResponse(StudentPage.render(context, request))
            else:
                context = {
                    'error' : "Wrong"
                }
                return HttpResponse(HomePage.render(context, request))
            
        except Exception as e:
            context['error'] = f"Error11: {str(e)}"
            return HttpResponse(HomePage.render(context, request))
        
def UpdateDetails(request):
    StudentPage = loader.get_template('StudentLogin.html')
    if request.method == 'POST': 
        FullName = request.POST.get('StudentName')
        RollNo = request.POST.get('StudentRollNo')
        UpdateMobileNo = request.POST.get('UpdateMobileNo')
        UpdatePassword = request.POST.get('UpdatePassword')
        
        try:
            image = models.Posters.objects.all()
            user = models.Student.objects.filter(FullName = FullName, RollNo = RollNo).first()
            Class = user.Class
            TimeTable = models.TimeTable.objects.filter(Class = Class).first()
            #Attendence = models.Attendence.objects.filter(RegNo = user.RollNo)
            user.MobileNo = UpdateMobileNo
            user.Password = UpdatePassword
            user.save()
            context = {
                'success' : 'Successfully Updated',
                'Student': FullName,
                    'image' : image,
                    'data' : {
                        'FullName': user.FullName,
                        'RollNo' : user.RollNo,
                        'MobileNo': user.MobileNo,
                        'Password': user.Password,
                        'Class': user.Class
                    },
                    'TimeTable' : TimeTable.Image,
                    #'Attendence' : Attendence
            }
            return HttpResponse(StudentPage.render(context, request))
        
        except Exception as e:
            context['Success'] = f"Error: {str(e)}"
            return HttpResponse(StudentPage.render(context,request))
        
def Attendence(request):
    StudentPage = loader.get_template('StudentLogin.html')
    image = models.Posters.objects.all().values()
    context = {}
    if request.method == 'POST':
        StudentRollNo = request.POST.get('StudentRollNo')
        StudentName = request.POST.get('StudentName')
        month1 = request.POST.get('month')
        year,month = map(int,month1.split('-'))
        user = models.Student.objects.filter(FullName = StudentName, RollNo = StudentRollNo).first()
        TimeTable = models.TimeTable.objects.filter(Class = user.Class).first()
        Subjects = models.Subject.objects.filter(Class = user.Class)
        FeeDetails = Smodels.FeeDetails.objects.filter(StudentRollNo = user.RollNo, StudentName = user.FullName).first()
        Data = models.AttendenceDetails.objects.filter(RegNo = StudentRollNo, AttendenceDate__year = year, AttendenceDate__month = month).values()
        PresentDays1 = models.AttendenceDetails.objects.filter(RegNo = StudentRollNo, AttendenceDate__year = year, AttendenceDate__month = month, Attendence = 'P').values()
        TotalWorkingDays = Data.count()
        PresentDays = PresentDays1.count()
        context = {
            'Date' : month1,
            'Month' : month,
            'WorkingDays' : TotalWorkingDays,
            'Present' : PresentDays,
            'image' : image,
            'data' : {
                'FullName': user.FullName,
                'RollNo' : user.RollNo,
                'MobileNo': user.MobileNo,
                'Password': user.Password,
                'Class': user.Class
            },
            'TimeTable' : TimeTable.Image,
            
            'Subjects' : Subjects,
            'FeeDetails' : FeeDetails

        }
        return HttpResponse(StudentPage.render(context, request))
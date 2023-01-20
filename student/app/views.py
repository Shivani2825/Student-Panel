from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password,make_password
from .models import User, Course, Student, Teacher
from django.http import  HttpResponse
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def user(request):
    return render(request,'sign-up.html')

def index(request):
    return render(request,'index.html')

def courses(request):
    
    data=Course.objects.all()
    return render(request,'courses.html',{"data":data})

def dashboard(request):
    return render(request,'dashboard.html')

def salaryslip(request):
    teacher=Teacher.objects.all()
    return render(request,'salaryslip.html',{'teacher':teacher})

def salarydash(request):
    # teacher=Teacher.objects.all()
    return render(request,'salarydashboard.html')

    
    
def teacher(request):
    teacher=Teacher.objects.all()
    return render(request,'teacher.html',{'teacher':teacher})
   

def student(request):
    student=Student.objects.all()
    data=Course.objects.all()
    return render(request,'viewstudents.html',{'student':student,'data':data})


# USER Registration------------------------------------------------------------------------------

def formdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            messages.error("ALREADY EXISTS")
            return redirect('/inde/')
        else:
            user=User.objects.create(name=name,email=email,password=password)
            user.save()
            return redirect('/inde/')
    return redirect('/inde/')
# Login--------------------------------------------------------------------------------
def loginform(request):
    if request.method == "POST":
        email = request.POST['email']
        User_password = request.POST['password']
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password
            if check_password(User_password, password):
                return redirect('/dashboard/')
            else:
                messages.error(request, 'Password incorrect')
                return redirect('/inde/')
        else:
            messages.error(request, 'Email is not registered')
            return redirect('/inde/')
    else:
        return redirect('/inde/')


# COURSES----------------------------------------------------------------

def addcourse(request):
    if request.method=='POST':
        cr=request.POST['course']
        Duration=request.POST['duration']
        Fees=request.POST['fees']
        Comment=request.POST['comment']
        if Course.objects.filter(coursename=cr).exists():
            messages.error(request,"ALREADY EXISTS")
            data=Course.objects.all()
            return render(request,'courses.html',{"data":data})
        else:
            data=Course.objects.create(coursename=cr,courseduration=Duration,coursefees=Fees,coursetextbox=Comment)
            data.save()
            messages.success(request,"Added Succesfully")
            data=Course.objects.all()
            return render(request,'courses.html',{"data":data})
    return redirect('/courses/')

def updatecourse(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        course = request.POST['name']
        duration = request.POST['duration']
        fees = request.POST['fees']
        comment= request.POST['comment']
        Course.objects.filter(id=uid).update(coursename=course,courseduration=duration,coursefees=fees,coursetextbox=comment)
        return redirect('/courses/')


def delete(request):
    cid=request.GET['cid']
    Course.objects.get(id=cid).delete()
    data=Course.objects.all()
    return render(request,'courses.html',{'data':data})

def update_view(request, uid):
    res = Course.objects.get(id=uid)
    return render(request, 'updatecourse.html', context={

        'course': res,
    })   


# STUDENT------------------------------------------------------------------------------------

def addstudent(request):
    j=Student()
    j.studentname=request.POST['name']
    j.studentemail=request.POST['email']
    j.studentmobile=request.POST['mobile']
    j.studentdegree=request.POST['degree']
    cid=request.POST['course']
    j.studentcourse=Course.objects.get(id=cid)
    j.save()
    student=Student.objects.all()
    data=Course.objects.all()
    return render(request,"viewstudents.html",{'student':student,'data':data})
   
def deletestudent(request):
    sid=request.GET['sid']
    Student.objects.get(id=sid).delete()
    data=Student.objects.all()
    return render(request,'viewstudents.html',{'data':data})



def update_student(request,uid):
    if request.method == 'POST':
        studentObj=Student()
        uid = uid
        studentObj.id=uid
        studentObj.studentname = request.POST['name']
        studentObj.studentemail = request.POST['email']
        studentObj.studentmobile = request.POST['mobile']
        studentObj.studentdegree= request.POST['degree']
        id= request.POST['course']
        studentObj.studentcourse=Course.objects.get(id=id)
        studentObj.save()
        student=Student.objects.all()
        return render(request,'viewstudents.html',{'student':student})

def updatestu(request,uid):
    id=uid
    res = Student.objects.get(id=id)
    data=Course.objects.all()
    return render(request, 'updatestudent.html', context={
        'stu':res,
        'data':data
    })
    
    

# TEACHER-----------------------------------------------------------------------------------



def addteacher(request):
    if request.method=='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Mobile=request.POST['mobile']
        Education=request.POST['education']
        Joindate=request.POST['joindate']
        Workexp=request.POST['workexp']
        Ctc=request.POST['ctc']
        if Teacher.objects.filter(teacheremail=Email).exists():
            messages.error(request,"ALREADY EXISTS")
            teacher=Teacher.objects.all()
            return render(request,'teacher.html',{'teacher':teacher})
        else:
            teacher=Teacher.objects.create(teachername=Name,teacheremail=Email,teachermobile=Mobile,education=Education,joindate=Joindate,workexp=Workexp,ctc=Ctc)
            teacher.save()
            messages.success(request,"Added Succesfully")
            teacher=Teacher.objects.all()
            return render(request,'teacher.html',{'teacher':teacher})
    return redirect('/teacher/')
      



def update_tech(request,uid ):
    res = Teacher.objects.get(id=uid)
    return render(request, 'update_tech.html', context={

        'teacher': res,
    })

def updateteacherdata(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        Name = request.POST['name']
        Email = request.POST['email']
        Mobile = request.POST['mobile']
        Education= request.POST['education']
        Joindate= request.POST['joindate']
        Work= request.POST['workexp']
        CTC= request.POST['ctc']
        Teacher.objects.filter(id=uid).update(teachername=Name,teacheremail=Email,
                                            teachermobile=Mobile,education=Education,
                                            joindate=Joindate,workexp=Work,ctc=CTC)
        return redirect('/teacher/')

def deleteteacher(request):
    tid=request.GET['tid']
    Teacher.objects.get(id=tid).delete()
    teacher=Teacher.objects.all()
    return render(request,'teacher.html',{'teacher':teacher})

# Logout---------------------------------------------------------------------------------------
def logout(request):
    auth.logout(request)
    messages.warning(request,'sucessfully logout')
    return redirect('/')


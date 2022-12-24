from django.db import models

class User(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=500, blank=True, null=True)
    is_active=models.BooleanField(default=True)


class Course(models.Model):
    coursename = models.CharField(max_length=200)
    coursefees=models.IntegerField()
    courseduration=models.CharField(max_length=100)
    coursetextbox=models.TextField()
    is_active=models.BooleanField(default=True)

class Student(models.Model):
    studentname=models.CharField(max_length=300)
    studentemail=models.CharField(max_length=200)
    studentmobile=models.IntegerField()
    studentdegree=models.CharField(max_length=200)
    studentcourse=models.ForeignKey(Course,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)

class Teacher(models.Model):
    teachername=models.CharField(max_length=300)
    teacheremail=models.CharField(max_length=200)
    teachermobile=models.IntegerField()
    joindate=models.DateField()
    education=models.CharField(max_length=200)
    workexp=models.CharField(max_length=200)
    ctc=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
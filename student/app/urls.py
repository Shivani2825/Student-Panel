from django.urls import path
from . import views

urlpatterns = [
    path('',views.user),
    path('inde/',views.index),
    path('courses/',views.courses),
    path('update_view/<int:uid>/',views.update_view, name='Updatecourse'),
    path('student/',views.student),
    path('formdata/',views.formdata),
    path('login/',views.loginform, name = 'datalogin'),
    path('dashboard/',views.dashboard),
    path('addcourse/',views.addcourse),
    path('deletecourse/',views.delete),
    path('addstudent/',views.addstudent),
    path('updatecourse/',views.updatecourse),
    path('deletestudent/',views.deletestudent),
    path('teacher/',views.teacher),
    path('addteacher/',views.addteacher),
    path('deleteteacher/',views.deleteteacher),
    path('update_tech/<int:uid>/',views.update_tech),
    path('updateteacherdata/',views.updateteacherdata),
    path('update_student/<int:uid>',views.update_student,name='update'),
    path('updatestu/<int:uid>',views.updatestu,name="update"),
    path('logout/',views.logout),


    

]

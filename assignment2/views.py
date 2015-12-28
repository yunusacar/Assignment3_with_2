from django.shortcuts import render



from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect
from django.template import RequestContext
from assignment2.models import*
from assignment2.Forms import *

# Create your views here.
def addteacher(request):
    form=teacherform()
    if request.method=='POST':
        form = teacherform(request.POST)
        if form.is_valid():
            a=teacher(fn=form.cleaned_data["fn"],ls=form.cleaned_data["ls"],email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-teachers/')
        else:
            form=teacher()
    return render_to_response('Teacher.html',{'form':form},RequestContext(request))

def Teacherlist(request):
    return render_to_response('Teacherlist.html',
    {'Teacherlist': teacher.objects.all()})

def addstudent(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            b=student(fn=form.cleaned_data["fn"],ls=form.cleaned_data["ls"],crs=form.cleaned_data["crs"],email=form.cleaned_data["email"])
            b.save()
            return HttpResponseRedirect('/all-students/')
        else:
            form=student()
    return render_to_response('Student.html',{'form':form},RequestContext(request))

def Studentlist(request):
    return render_to_response('Studentlist.html',{'Studentlist':student.objects.all()})

def addcourse(request):
    form=courseform()
    if request.method=='POST':
        form=courseform(request.POST)
        if form.is_valid():
            c= course(name=form.cleaned_data["name"],code=form.cleaned_data["code"],croom=form.cleaned_data["croom"],time=form.cleaned_data["time"],tc=form.cleaned_data["tc"])
            c.save()
            return HttpResponseRedirect('/all-courses/')
        else:
            form=course()
    return render_to_response('Course.html',{'form':form},RequestContext(request))

def Courselist(request):
    return render_to_response('Courselist.html',{'Courselist':course.objects.all()})
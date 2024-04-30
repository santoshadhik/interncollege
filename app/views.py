from django.shortcuts import render,HttpResponsePermanentRedirect
from .form import StudentRegistration
from .models import User
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def add_show(request):
    if(request.method == 'POST'):
        fm=StudentRegistration(request.POST)
        
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            epw= make_password(pw)
            reg= User(name=nm,email=em,password=epw)
            reg.save() 
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
     
       
    return render(request,"app/add.html",{'key': fm,'stu':stud})
#this function will delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect('/add')
    
#this function will update
def update_data(request,id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            epa=make_password(pw)
            pi.name= nm
            pi.email=em
            pi.password=pw

            pi.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'app/update.html',{'d':fm})


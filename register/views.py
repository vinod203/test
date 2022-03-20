from django.shortcuts import render,redirect
from django.views.generic import UpdateView
from django.contrib import messages

from django.http import HttpResponse
from register.forms import StudentForm, SForm
from register.models import Student
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



class StudentCRUDView(View):
    def get(self,request):
        list = Student.objects.all()
        return render(request,'register/stud_list.html',{'list':list})

    def post(self,request):
        if request.method == 'POST':
            form = StudentForm(request.POST or None)
            if form.is_valid():
                form.save()
        else:
            form=StudentForm()
            return render(request,'register/stud_reg.html',{'form':form})

def home(request):
    return render(request ,'register/index.html')

@login_required(login_url='login')
def stud_register(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        email = form.cleaned_data['semail']
        # mob = form.cleaned_data['smob']
        addr = form.cleaned_data['saddr']
        res = Student.objects.filter(sname=name,)
        if len(res)>0:
            messages.success(request, f' {name}  already Registered')
            # return render(request, 'register/ack.html', {'title': 'Student details already exists'})
        else:
            p = Student(sname=name,semail = email,saddr=addr)
            p.save()

            messages.success(request,f' {name} Registered successfully')

            # return render(request,'register/ack.html',{'title':'Registered Successfully'})
    my_dict = {

        'form':form
    }
    return render(request,'register/stud_reg.html',my_dict)

def stud_update(request,pk):
    title = 'Student Update'
    form = StudentForm(request.POST)

    my_dict = {
        'title': title,
        'form': form
    }
    return render(request, 'register/stud_reg.html', context=my_dict)

@login_required(login_url='login')
def stud_delete(request):
    title='Student Delete'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        list = Student.objects.filter(sname=name)
        if len(list)==0:
            return render(request,'register/ack.html',{'title':'Student details not found please enter correct details'})
        else:
            list= Student.objects.filter(sname=name).delete()
            return render(request,'register/ack.html',{'title':'Student deleted successfully'})
    context ={
        'title':title,
        'form':form
    }
    return render(request,'register/delete.html',context)


def stud_all(request):
    title ='Registered Students'
    list = Student.objects.all()
    context = {
        'title':title,
        'list':list
    }
    return render(request,'register/stud_list.html',context)

# class StudentListView(ListView):
#     model = Student
#     template_name = 'register/student_list.html'
#     context_object_name = 'student'



def stud_search(request):
    title = 'Search Student'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        list=Student.objects.filter(sname=name)
        if len(list)==0:
            return render(request,'register/ack.html',{'title':'Student details not found try another'})
        my_dict={
            'title':title,
            'list':list
        }
        return render(request,'register/stud_list.html',my_dict)
    my_dict = {
        'title': title,
        'form': form
    }
    return render(request,'register/search.html',my_dict)



class StudentUpdateView(UpdateView):
    model = Student
    fields = [
        "sname","saddr","sdep","ssch"
    ]
    template_name = 'register/student_update.html'
    success_url = "/stud-all"


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            messages.success(request,f'Your account has been created successfully for {username} you can login now')
            return redirect('login')

    else:
        form=UserCreationForm()
    return render(request,'register/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'register/profile.html')


# api

def emp_data_view(request):
    emp_data = {
        'eno':5000,
        'ename':'rao',
        'esal':50000,
        'eaddr':'bglr'
    }
    response = '<h1>Employee no:{}<br>Employee name:{}<br>Employee salary:{}<br>Employee address:{}'.format(emp_data['eno'],emp_data['ename'],emp_data['eaddr'],emp_data['esal'])
    return HttpResponse(response)

import json
def emp_data_jsonview(request):
    emp_data = {
        'eno':5000,
        'ename':'rao',
        'esal':50000,
        'eaddr':'bglr'
    }
    json_data = json.dumps(emp_data)
    response = '<h1>Employee no:{}<br>Employee name:{}<br>Employee salary:{}<br>Employee address:{}'.format(emp_data['eno'],emp_data['ename'],emp_data['eaddr'],emp_data['esal'])
    return HttpResponse(json_data,content_type='application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data = {
        'eno':5000,
        'ename':'rao',
        'esal':50000,
        'eaddr':'bglr'
    }
    return JsonResponse(emp_data)

from django.views.generic import View
from rest_framework.response import Response

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data = {
            'eno': 5000,
            'ename': 'rao',
            'esal': 50000,
            'eaddr': 'bglr'
        }
        return JsonResponse(emp_data)

from rest_framework.views import APIView
from register.serializers import StudentSerializer

class StudentListView(APIView):
    def get(self,requst):
        q = Student.objects.all()
        serializer = StudentSerializer(q,many=True)
        return Response(serializer.data)
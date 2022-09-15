from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import empolyee,  role ,department
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomerRegistrationForm
from django.views import View
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login
from django.shortcuts import HttpResponseRedirect




def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps= empolyee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      sallary=int(request.POST['sallary'])
      bonus=int(request.POST['bonus'])
      phone=int(request.POST['phone'])
      role=int(request.POST['role'])
      hire_date=request.POST['hire_date']
      dept=int(request.POST['dept'])

      new_emp=empolyee(first_name = first_name , last_name = last_name, sallary= sallary , bonus = bonus , phone= phone, role_id = role, hire_date= datetime.now(), dept_id=dept )
      new_emp.save()
      return HttpResponse('empolyee added successfully')

    elif request.method =='GET':
         return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Empolyee ")

def remove_emp(request, emp_id = 0):

    if emp_id:
        try:
            emp_to_be_removed = empolyee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Empolyee removed successfully")
        except:
            return HttpResponse("plz enter a valid emp id")

    emps= empolyee.objects.all()
    context = {

    'emps':emps
  }
    print(context)
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method =='POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = empolyee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)

        context ={
           'emps': emps

        }
        print(context)
        return render(request, 'all_emp.html',context)

    elif  request.method == 'GET':
          return render (request, 'filter_emp.html')

    else: 
         return HttpResponse('An Exception Occured')





class CustomerRegistrationView(View):
 def get(self, request):
  forms = CustomerRegistrationForm()
  return render(request, 'userregistration.html', {'form':forms})
  
 def post(self, request):
  forms = CustomerRegistrationForm(request.POST)
  if forms.is_valid():
   messages.success(request, 'Congratulations!! Registered Successfully.')
   forms.save()
  return render(request, 'userregistration.html', {'form':forms})



def user_login(request):
 if request.method =='POST':
   fn = AuthenticationForm(request=request, data=request.POST)
   if fn.is_valid():
    uname = fn.cleaned_data['username']
    upass = fn.cleaned_data['password']
       
    user= authenticate(username=uname, password=upass)  
    if user is not None:
      login(request,user)
      return render(request,'login.html')
 else: 
    fn=AuthenticationForm()
 
    return render( request,'login.html',{'form':fn})























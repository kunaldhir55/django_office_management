from django.shortcuts import render,HttpResponse
from .models import Employee,Department,Role
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emp = Employee.objects.all()
    print(f'add emp dept: {emp}')
    context = {
        'emps':emp
    }
    return render(request,'all_emp.html',context)


def add_emp(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']
        salary = int(request.POST['salary'])
        bounus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']
        new_emp = Employee(first_name=first_name,last_name=last_name,dept_id=dept,role_id=role,salary=salary,bonus=bounus,phone=phone,hire_date=hire_date)
        new_emp.save()
        HttpResponse('Employee added successfully')
        
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        HttpResponse('Exception occured while adding employee')
    

def remove_emp(request,emp_id=0):
    
    if emp_id:
        try:
            emp_removed  = Employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse('Employee has been removed.')
        except:
            return HttpResponse('Please enter valid Emp id')

    emp = Employee.objects.all()
    context = {
        'emps':emp
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {

            'emps':emps
        }
        return render(request,'all_emp.html',context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        HttpResponse('Exception occured in filter view.')
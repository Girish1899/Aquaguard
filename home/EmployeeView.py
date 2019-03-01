# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .views import success,fail
from .models import Employee, EmpTarget
from django.shortcuts import HttpResponse
import datetime


@csrf_exempt
def createNewEmployee(request):
    if (request.method=="POST"):
        first_name=request.POST.get("fname",None)
        last_name=request.POST.get("lname",None)
        phone=request.POST.get("phone",None)
        email=request.POST.get("mail",None)
        print(phone)
        print(first_name)
        print(email)
        if(first_name == None or last_name==None or phone==None or email==None):
           return fail("Invalid details")
        else:
            employee = Employee(first_name=first_name, last_name=last_name, phone=phone, email=email,type="tc")
            employee.save()
            return success("New employee created!")
    return HttpResponse("Invalid Page")


def displayAllEmployee(request):
    employees=Employee.objects.filter(isActive=True)
    print(employees)
    print("DATA IS OUTPUTTED OVER HERE")
    employee_list=[]
    print(len(employees))
    if(len(employees)==0):
        return fail("No employee in db")
    else:
        for i in range(len(employees)):
            emp={}
            emp['fname']=employees[i].first_name
            emp['lname']=employees[i].last_name
            emp['email']=employees[i].email
            emp['phone']=employees[i].phone
            emp['category']=employees[i].type
            emp['id']=employees[i].id
            emp['pincode']=employees[i].pincode
            employee_list.append(emp)

        return success(employee_list)


@csrf_exempt
def deactivateEmployee(request):
    if request.method =='POST':
        employee_id=request.POST['employee_id']
        if(not(employee_id==None)):
            employee=Employee.objects.get(id=employee_id)
            if(not(employee==None)):
                employee.isActive=False
                employee.save()
                return success("Employee deactivated successfully")


    return fail("unable to delete employee")

def editEmployee(request):
    if (request.method=="POST"):
        first_name=request.POST.get("fname",None)
        last_name=request.POST.get("lname",None)
        phone=request.POST.get("phone",None)
        email=request.POST.get("mail",None)
        id=request.POST.get("id",None)
        print(phone)
        print(first_name)
        print(email)
        if(first_name==None and last_name==None and phone==None and email==None):
           return fail("Invalid details")
        else:
            employee = Employee(first_name=first_name, last_name=last_name, phone=phone, email=email,type="tc")
            employee.save()
            return success("New employee created!")
    return HttpResponse("Invalid Page")

@csrf_exempt
def uploadEmployeeProfilePic(request):
    if(request.method=="POST"):
        id=request.POST.get("id", None)
        if id == None or id == '':
            try:
                emp = Employee.objects.get(empID=id)
                emp.profilePicture=request.FILES['profile_pic']
                emp.save()
                return success("success")
                # return success("profile image saved at "+emp.profilePicture)
            except Exception as e:
                print(e)
                return fail("failed")
    return fail("Bad request")

@csrf_exempt
def setEmpTarget(request):
    if request.method=="POST":
        currDate = str(datetime.datetime.now().date())
        emp_id = request.POST.get("id", None)
        if emp_id == None or emp_id == '':
            return fail("employee id hasn't provided")
        try:
            empObj = Employee.objects.get(empID = emp_id)
        except Exception as e:
            print(e)
        callTarget = request.POST.get("callTarget", None)
        commitTarget = request.POST.get("commitTarget", None)
        endDate = request.POST.get("endDate", None)

        # Just incase if they don't want to use the progress bar.
        if callTarget == None:
            callTarget = 0
        if commitTarget == None:
            commitTarget = 0
        try:
            targetObj =  EmpTarget.objects.get(employeeID = empObj)
        except Exception as e:
            # if no employee there in the table the try would fail.
            targetObj = EmpTarget()
            targetObj.employeeID = empObj
            targetObj.callTarget = callTarget
            targetObj.commitTarget = commitTarget
            targetObj.startDate = currDate
            targetObj.endDate = endDate
        # if the employee data already exist in the the table do this
        targetObj.callTarget = callTarget
        targetObj.commitTarget = commitTarget
        targetObj.startDate = currDate
        targetObj.endDate = endDate
        targetObj.save()
        return success("Target has been saved")
    return fail("Error in request")
















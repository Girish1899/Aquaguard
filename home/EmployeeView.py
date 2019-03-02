# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .views import success,fail
from .models import Employee, EmpTarget, Leads
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
        emp_id=request.POST.get("id", None)
        if emp_id == None or emp_id == '':
            return fail("Employee id not provided")
        try:
            empObj = Employee.objects.get(id = emp_id)
        except Exception as e:
            return fail("Employee doesn't exist")
        empObj.isActive=False
        empObj.save()
        return success("Employee deactivated successfully")
    return fail("Error in request")


@csrf_exempt
def getSingleEmployee(request):
    if (request.method == "POST"):
        emp_id = request.POST.get("id",None)
        empObj = Employee.objects.get(id=emp_id)
        employee = {}
        employee['fname'] = empObj.fname
        employee['lname'] = empObj.lname
        employee['email'] = empObj.email
        employee['phone'] = empObj.phone
        employee['address'] = empObj.address
        employee['isActive'] = empObj.purchaseDate
        employee['profilePicture'] = empObj.pincode
        employee['role'] = empObj.comments
        return success(employee)
    return HttpResponse("Error In Request")

@csrf_exempt
def updateEmployee(request):
    if (request.method == "POST"):
        emp_id = request.POST.get("id", None)
        fname = request.POST.get("fname", None)
        lname = request.POST.get("lname", None)
        phone = request.POST.get("phone", None)
        email = request.POST.get("mail", None)
        pincode = request.POST.get("pincode", None)
        address = request.POST.get("address", None)
        image=request.FILES.get("profilePic",None)

        if emp_id == None or emp_id == '':
            return fail("Employee id is not provided")

        empObj = Employee.objects.get(empID = emp_id)
        if fname is not None:
            empObj.fname = fname
        if lname is not None:
            empObj.lname = lname
        if phone is not None:
            empObj.phone = phone
        if email is not None:
            empObj.email = email
        if pincode is not None:
            empObj.pincode = pincode
        if address is not None:
            empObj.address = address
        if image is not None:
            empObj.profilePicture= image
        empObj.save()
        return success("Employee information updated")
    return fail("Error in request")



@csrf_exempt
def uploadEmployeeProfilePic(request):
    print(request.POST)
    print(request.FILES)
    if(request.method=="POST"):
        id=request.POST.get("id", None)
        if id is not None:
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



@csrf_exempt
def assignLeads(request):
    if request.method=="POST":
        # currDate = str(datetime.datetime.now().date())
        emp_id = request.POST.get("id", None)
        if emp_id == None or emp_id == '':
            return fail("employee id hasn't provided")
        try:
            empObj = Employee.objects.get(empID = emp_id)
        except Exception as e:
            print(e)
        startRow = request.POST.get("startRow", None)
        endRow = request.POST.get("endRow", None)
        leads = Leads.objects.filter(id__range(startRow, endRow))
        for lead in leads:
            lead.assignee = empObj
            lead.save()
        return success("Successfully assigned")
    return fail("Error in request")

        















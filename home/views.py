from django.shortcuts import render,HttpResponse
# from home.models import Employee,Customer,CurrentBooking,Product
from home.models import Employee, Customers, Product

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json



#ANDROID LOGIN
@csrf_exempt
def login(request):
    if(request.method=='POST'):
        phone=request.POST.get("username",None)
        password=request.POST.get("password",None)
        if(phone==None and password==None):
            fail("Invalid credentials")
        else:
            technician_data = Employee.objects.filter(phone=phone, password=password, type='tn')
            if (len(technician_data) > 1):
                return HttpResponse("User Valid")
            else:
                return HttpResponse("User Invalid")

    return HttpResponse("Login is successful")


#TECHNICIAN REGISTRATION
@csrf_exempt
def registration(request):
    if(request.method=='POST'):
        #FETCH ALL DATA FROM THE USER
        phone,password,pincode,username=request.POST.get("phone",None),request.POST.get("password",None),request.POST.get("pincode",None),request.POST.get("username",None)
        #VALIDATE IF ALL THE DATA EXISTS
        print(phone)
        print(password)
        print(pincode)
        print(username)
        if(phone==None and password==None and pincode==None and username==None):
            return fail("invalid request")
        else:
            try:
                technician=Employee(phone=phone,password=password,name=username,pincode=pincode, type='tn')
                technician.save()
                return success("New user registered")
            except:
                return fail("database error")
    return HttpResponse("Invalid page")



def success(message):
    output = {}
    output["result"] = "success"
    output["description"] = message
    return HttpResponse(json.dumps(output))

def fail(message):
    output={}
    output["result"] = "fail"
    output["description"] = message
    return HttpResponse(json.dumps(output))


#changes made here for tesint purpose only






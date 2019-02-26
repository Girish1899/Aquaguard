from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
from .views import success,fail
from .models import Customers, Employee, Leads, EmpStatus
from django.shortcuts import HttpResponse, render
from .tests import cleanDatabase, fill_database_with_dummy_values

from django.utils import timezone
import pytz
import json
import datetime





#----------------------- Page Renders ---------------------------#
@csrf_exempt
def loginPage(request):
    return render(request, 'loginPage.html')


@csrf_exempt
def homePage(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        loginPage(request)
    return render(request, 'tempHomePage.html')


@csrf_exempt
def homePageCommittedLeads(request):
    return render(request, 'committedLeads.html')


@csrf_exempt
def homePageContactLeads(request):
    return render(request, 'contactLeads.html')


@csrf_exempt
def logoutPage(request):
    return render(request, 'logoutPage.html')


@csrf_exempt
def changedp(request):
    return render(request, 'change_dp.html')
#----------------------- Api's ---------------------------#


@csrf_exempt
def storeSession(request):
    id=request.POST.get("id", None)
    if(id == None or id == ''):
        return fail("Haven't received any emp_id to create session")
    else:
        try:
            request.session['emp_id'] = id
            return success('Session has been created') 
        except Exception as e:
            return fail("Employee Id Not Foud")


    
@csrf_exempt
def getSession(request, isLocalUse=None):
    if (request.method == "POST"):
        if isLocalUse:
            if 'emp_id' in request.session:
                sessionID = request.session['emp_id']
                return sessionID
            return ''
        else:
            if 'emp_id' in request.session:
                sessionID = request.session['emp_id']
                if (sessionID == ''):
                    return fail("You need to login")
                return success(sessionID)
            return fail("You need to login")
    return fail("Bad request")



@csrf_exempt
def flushSession(request, isLocalUse=None):
    if (request.method == "POST"):
        request.session.flush()
        return success("Session cleared")


@csrf_exempt
def getUserData(request):
    if (request.method == "POST"):
        id=request.POST.get("id", None)
        if id == None or id=='':
            return fail("Enter Employee Id")
        try:
            #get his first and lastname
            employee = Employee.objects.get(empID = id)
        except Exception as e:
            return fail("Employee Id Not Foud")

        empStatus = getEmpLogInfo(employee)
        if empStatus != None:
            loginTime = empStatus.loginTime
        else:
            loginTime = None

        dataReturn = {
            "fname": employee.fname,
            "lname": employee.lname,
            "loginTime": loginTime
        }
        return success(dataReturn)


    return fail("Invalid method")



@csrf_exempt
def storeEmpLog(emp, isLoggingIn):
    timeNow = datetime.datetime.now()
    dateToString = str(datetime.datetime.now().date())
    if isLoggingIn is True:
        try:
            # The try would pass if it isn't a new employee, else there wont be an entry with date column
            empStatus = EmpStatus.objects.get(employeeID = emp, date = str(datetime.datetime.now().date()))

            # If it is a new day the login timstamp need to be stored
            if empStatus.date != str(datetime.datetime.now().date()):
                empStatus.employeeID = emp
                empStatus.loginTime = timeNow
                empStatus.date = dateToString
                empStatus.save()

                #employee made active
                emp.isActive = True
        except Exception as e:
            # This is for a new employee.
            empStatus = EmpStatus()
            empStatus.employeeID = emp
            empStatus.loginTime = timeNow
            empStatus.date = dateToString
            empStatus.save()

            #employee made active
            emp.isActive = True

    else:
        empStatus.logoutTime = timeNow
        empStatus.save()

        #employee made inactive
        emp.isActive = False

        # print("This is the time now")
        # print(timeNow.time().replace(second=0, microsecond=0))
        # print(timeNow.date())

# @csrf_exempt
# def date_handler(obj):
#     if hasattr(obj, 'isoformat'):
#         return obj.isoformat()
#     else:
#         raise TypeError
#     print json.dumps(data, default=date_handler)

@csrf_exempt
def getEmpLogInfo(empInstance):
    try:
        # today = timezone.now()
        # today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        empStatus = EmpStatus.objects.get(employeeID = empInstance, date = str(datetime.datetime.now().date()))
        # Taking only initial login time. there can be multiple logins.
        # print(empStatus[0])
        if empStatus == None:
            return None
        return empStatus
    except Exception as e:
        print(e)


@csrf_exempt
def empLoginCheck(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        if id == None or id == '':
            return fail("Enter Employee Id")
        else:
            try:
                employee = Employee.objects.get(empID = id)

            except Exception as e:
                return fail("Employee Id Not Foud")
                
            #handle session here
            storeSession(request)

            #store employee login information here.
            storeEmpLog(employee, True)

            return success('employee logged in')
    return fail("Bad Request")

@csrf_exempt
def storeLogoutTime(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        if id == None or id == '':
            return fail("Provide employee id")
        else:
            timeNow = str(datetime.datetime.now())
            dateToday = str(datetime.datetime.now().date())
            employee = Employee.objects.get(empID = id)
            empStatus = EmpStatus.objects.get(employeeID = employee, date = dateToday)
            empStatus.logoutTime = timeNow
            empStatus.save()
        return success("logoutTime has been saved")
    return fail("Bad request")


@csrf_exempt
def addNewLead(request):
    if (request.method == "POST"):
        fname = request.POST.get("fname",None)
        lname = request.POST.get("lname",None)
        mobile = request.POST.get("mobile",None)
        email = request.POST.get("email",None)
        address = request.POST.get("address",None)
        pincode = request.POST.get("pincode",None)
        land = request.POST.get("land",None)
        alternativeMobile = request.POST.get("alternativeMobile",None)
        if(fname == None or lname ==  None or mobile ==  None or email ==  None or
                address ==  None or pincode ==  None or land ==  None or alternativeMobile ==  None):
           return fail("Invalid details")
        else:
            lead = Customer(fname = fname, lname = lname, mobile = mobile, email = email,
            	address = address, pincode = pincode,land = land, alternativeMobile = alternativeMobile)
            lead.save()
            return success("New Lead created!")
    return fail("Invalid Admin Page")


# This should get you all leads that you have given to deal with
@csrf_exempt
def getAssignedLeads(request):
    if request.method == "POST":
        id = request.POST.get("id", None)
        if id != None:
            try:
                employee = Employee.objects.get(empID=id)
            except Exception as e:
                return fail("Employee Id Not Foud")
            # tip: leads = CustomerEmployee.objects.filter(employee=employee , status='ip')

            # we supposed to get all leads based on assignee is equal to empid
            # since it is a test its fine
            leads = Leads.objects.all()
            if len(leads) == 0:
                return fail("No leads in db")
            else:
                leads_list = []
                for lead in leads:
                    eachRow = {}
            #     for i in range(len(leads))
            #         lead={}
            #         lead['id']=leads[i].customer.id
                    eachRow['fname'] = lead.fname
                    eachRow['lname'] = lead.lname
                    eachRow['email'] = lead.email
                    eachRow['phone'] = lead.phone
                    eachRow['address'] = lead.address
                    eachRow['pincode'] = lead.pincode
                    leads_list.append(eachRow)
                return success(leads_list)
        return fail("Error In Request")


# This should get you all committed leads
@csrf_exempt
def getInterestedLeads(request):
    if request.method == "POST":
        leads = Leads.objects.all().filter(isInterested=True)
        print("length of leads", len(leads))
        if len(leads) == 0:
            return fail("No employee in db")
        else:
            leads_list = []
            for lead in leads:
                eachRow = {}
        #     for i in range(len(leads))
        #         lead={}
        #         lead['id']=leads[i].customer.id
                eachRow['fname'] = lead.fname
                eachRow['lname'] = lead.lname
                eachRow['email'] = lead.email
                eachRow['phone'] = lead.phone
                eachRow['address'] = lead.address
                eachRow['pincode'] = lead.pincode
                leads_list.append(eachRow)
            return success(leads_list)
    return fail("Error In Request")


# This should get you all leads yet to be called
@csrf_exempt
def getLeadsNotContacted(request):
    if request.method == "POST":
        leads = Leads.objects.all().filter(isContacted=False)
        if len(leads) == 0:
            return fail("No employee in db")
        else:
            leads_list = []
            for lead in leads:
                eachRow = {}
        #     for i in range(len(leads))
        #         lead={}
        #         lead['id']=leads[i].customer.id
                eachRow['fname'] = lead.fname
                eachRow['lname'] = lead.lname
                eachRow['email'] = lead.email
                eachRow['phone'] = lead.phone
                eachRow['address'] = lead.address
                eachRow['pincode'] = lead.pincode   
                leads_list.append(eachRow)
            return success(leads_list)
    return fail("Error In Request")




# @csrf_exempt
# def displaySingleLead(request):
#     if (request.method=="POST"):
#         id = request.POST.get("id",None)
#         leadObj=Customer.objects.get(id = id)
#         lead={}
#         lead['fname']=leadObj.fname
#         lead['lname']=leadObj.lname
#         lead['email']=leadObj.email
#         lead['mobile']=leadObj.mobile
#         lead['alternativeMobile']=leadObj.alternativeMobile
#         lead['address']=leadObj.address
#         lead['land']=leadObj.land
#         lead['pincode']=leadObj.pincode
#         lead['status']=leadObj.status
#         lead['comments']=leadObj.comments
#         return success(lead)
#     return HttpResponse("Error In Request")

# @csrf_exempt
# def getCallCount(request):
#     if (request.method=="POST"):
#         empid = request.POST.get("id",None)
#         if(empid != None):
#             try:
#                 employee = Employee.objects.get(id=empid)
#             except Exception as e:
#                 return fail("Employee Id Not Foud")
#             empObj = CallsPerDay.objects.filter(employee = employee , id = empid)
#             emp={}
#             emp['total']=empObj.totalCalls
#             emp['completed']=empObj.completedCalls
#             # return success(lead)
#             return success(emp)
#     return HttpResponse("Error In Request")

# @csrf_exempt
# def setCallCount(request):
#     if (request.method=="POST"):
#         empid = request.POST.get("id",None)

#         if(empid != None):
#             try:
#                 employee = Employee.objects.get(id=empid)
#             except Exception as e:
#                 return fail("Employee Id Not Foud")
#             empObj = CallsPerDay.objects.get(employee = employee)
#             count = empObj.completedCalls
#             count = count + 1
#             return success(lead)
#     return HttpResponse("Error In Request")
        
# @csrf_exempt
# def updateStatus(request):
#     if (request.method=="POST"):
#         id = request.POST.get("id",None)
#         status = request.POST.get("status",None)
#         comments = request.POST.get("comments",None)
#         if(id == None ):
#            return fail("No Id Found")
#         else:
#             lead = Customer.objects.get(id = id)
#             lead.status = status
#             lead.comments = comments
#             # lead = Customer(status = status, comments = comments)
#             lead.save()
#             return success("New Lead created!")
#     return HttpResponse("Error In Request")



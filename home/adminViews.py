from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
from .views import success, fail
from .models import Customers, Employee, Leads, EmpStatus, Notifications
from django.shortcuts import HttpResponse, render
from .tests import cleanDatabase, fill_database_with_dummy_values
from django.utils import timezone
from django.utils.dateparse import parse_date
# from django_otp.oath import hotp
import pytz
import json
import datetime
import pandas as pd

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


#----------------------- Page Renders ---------------------------#
@csrf_exempt
def loginPage(request):
    return render(request, 'loginPage.html')


@csrf_exempt
def homePage(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        loginPage(request)
    return render(request, 'index.html')


@csrf_exempt
def homePageCommittedLeads(request):
    return render(request, 'committedLeads.html')


@csrf_exempt
def homePageContactLeads(request):
    return render(request, 'contactLeads.html')

@csrf_exempt
def callHistoryPage(request):
    return render(request, 'call_history.html')


@csrf_exempt
def commitHistoryPage(request):
    return render(request, 'commits_board.html')

@csrf_exempt
def forgotPassword(request):
    return render(request, 'forgotpassword.html')


@csrf_exempt
def logoutPage(request):
    return render(request, 'logoutPage.html')


@csrf_exempt
def changedp(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        homePage(request)
    return render(request, 'change_dp.html')
#----------------------- Api's ---------------------------#


@csrf_exempt
def storeSession(request):
    id = request.POST.get("id", None)
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


# @csrf_exempt
# def generateOTP(request):
#     if (request.method == "POST"):
#         secret_key = b'1234567890123467890'
#         now = int(time.time())
#         for delta in range(10, 110, 20):
#             print(totp(key=secret_key, step=10, digits=6, t0=(now-delta)))

@csrf_exempt
def getUserData(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        if id == None or id == '':
            return fail("Enter Employee Id")
        try:
            # get his first and lastname
            employee = Employee.objects.get(empID=id)
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
def addProfilePicture(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        if id == None or id == '':
            return fail("Provide employee id")
        else:
            try:
                employee = Employee.objects.get(empID = id)
            except Exception as e:
                return fail("Employee Id Not Foud")
            employee.profile_logo = request.FILES['profile_logo']
            file_type = employee.profile_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return fail("Image file must be PNG, JPG, or JPEG")
            employee.save()            
        return success("Picture Uploaded Successfully")
    return fail("Bad request")


@csrf_exempt
def getProfilePicture(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        if id == None or id == '':
            return fail("Provide employee id")
        else:
            try:
                employee = Employee.objects.get(empID=id)
            except Exception as e:
                return fail("Employee Id Not Foud")
            return success(employee.profile_logo.url)
    return fail("Bad request")


@csrf_exempt
def setNotification(request):
    if (request.method == "POST"):
        noteForAll = False
        noteType = request.POST.get("noteType", None)
        date = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time())
        time = time[:8]
        id = request.POST.get("id", None)
        message = request.POST.get("message", None)
        if message == None or message == '':
            return fail("Message Cannot Be NULL")
        if id == None or id == '':
            noteForAll = True
            employee = None
        else:
            try:
                employee = Employee.objects.get(empID=id)
            except Exception as e:
                return fail("Employee Id Not Found")
        note = Notifications(message=message, date=date, employeeID=employee,
                             time=time, noteType=noteType, noteForAll=noteForAll)
        note.save()
        return success("Notification Successfully Triggered")
    return fail("Bad request")


@csrf_exempt
def getNotification(request):
    if (request.method == "POST"):
        noteForAll = False
        date = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time())
        time = time[:8]
        message = None
        id = request.POST.get("id", None)
        # noteType = request.POST.get("noteType", None)
        if id == None or id == '':
            employee = None
            noteForAll = True
        else:
            try:
                employee = Employee.objects.get(empID=id)
            except Exception as e:
                return fail("Employee Id Not Found")
        notes = Notifications.objects.all().filter(
            employeeID=employee, noteType=noteType, date=date, noteForAll=noteForAll)
        if len(notes) == 0:
            return fail("No Noification Today")
        else:
            notes_list = []
            for note in notes:
                eachRow = {}
                eachRow['message'] = note.message
                eachRow['time'] = note.time
                notes_list.append(eachRow)
            return success(notes_list)
    return fail("Bad request")


@csrf_exempt
def togglePause(request):
    if (request.method == "POST"):
        timeNow = str(datetime.datetime.now())
        currDate = str(datetime.datetime.now().date())

        emp_id = request.POST.get("id", None)
        isPause = request.POST.get("isPause", None)
        if emp_id == None or emp_id == '':
            return fail("Enter Employee Id")
        try:
            empObj = Employee.objects.get(empID=emp_id)
            empStatObj = EmpStatus.objects.get(employeeID=empObj, date=currDate)
        except Exception as e:
            print(e)
            return fail("Couldn't get desired object")
        else:
            if isPause == 'true':
                empStatObj.pauseTime = timeNow
                empStatObj.isPause = True
                empStatObj.save()
                return success("Pause time has been captured")
            if isPause == 'false':
                duration = calculatePauseDuration(empStatObj.pauseTime)
                empStatObj.pauseTime = ''
                empStatObj.isPause = False
                empStatObj.save()
                return success(duration)
    return fail("Error in request")

def calculatePauseDuration(pauseTime):
    timeNow = datetime.datetime.now()
    pTime = datetime.datetime.strptime(pauseTime, "%Y-%m-%d %H:%M:%S.%f")
    deltaObj = datetime.timedelta(hours=pTime.hour, minutes=pTime.minute, seconds=pTime.second)
    pauseDuration = timeNow - deltaObj
    return str(pauseDuration)

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
                emp.save()
        except Exception as e:
            # This is for a new employee.
            empStatus = EmpStatus()
            empStatus.employeeID = emp
            empStatus.loginTime = timeNow
            empStatus.date = dateToString
            empStatus.save()

            #employee made active
            emp.isActive = True
            emp.save()

    else:
        empStatus.logoutTime = timeNow
        empStatus.save()

        #employee made inactive
        emp.isActive = False
        emp.save()

        # print("This is the time now")
        # print(timeNow.time().replace(second=0, microsecond=0))
        # print(timeNow.date())


@csrf_exempt
def getEmpLogInfo(empInstance):
    try:
        currDate = str(datetime.datetime.now().date())
        
        # Taking only initial login time. there can be multiple logins.
        empStatus = EmpStatus.objects.get(employeeID = empInstance, date = currDate)
       
        if empStatus == None:
            return None
        return empStatus
    except Exception as e:
        print(e)


@csrf_exempt
def empLoginCheck(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        password = request.POST.get("password", None)
        if id == None or id == '':
            return fail("Enter Employee Id")
        else:
            try:
                employee = Employee.objects.get(empID = id)

            except Exception as e:
                return fail("Employee Id Not Foud")

            #password check
            if password != employee.password:
                return fail("Wrong password")
                
            #handle session here
            storeSession(request)

            #store employee login information here.
            storeEmpLog(employee, True)

            return success('employee logged in')
    return fail("Error in Request")


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


# If you want to manually add a lead
@csrf_exempt
def addNewLead(request):
    if (request.method == "POST"):
        fname = request.POST.get("fname", None)
        lname = request.POST.get("lname", None)
        mobile = request.POST.get("mobile", None)
        email = request.POST.get("email", None)
        address = request.POST.get("address", None)
        pincode = request.POST.get("pincode", None)
        alternatePhone = request.POST.get("alternatePhone", None)
        purchaseDate = request.POST.get("purchaseDate", None)
        if(fname == None or lname ==  None or mobile ==  None or email ==  None or
                address ==  None or pincode ==  None or purchaseDate == None or alternatePhone ==  None):
           return fail("Invalid details")
        lead = Leads(fname = fname, lname = lname, mobile = mobile, email = email,
            address = address, pincode = pincode, purchaseDate = purchaseDate, alternatePhone = alternatePhone)
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
                    eachRow['id'] = lead.id
                    eachRow['fname'] = lead.fname
                    eachRow['lname'] = lead.lname
                    eachRow['email'] = lead.email
                    eachRow['phone'] = lead.phone
                    eachRow['address'] = lead.address
                    eachRow['pincode'] = lead.pincode
                    eachRow['isInterested'] = lead.isInterested
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

@csrf_exempt
def setCommit(request):
    if request.method == "POST":
        lead_id = request.POST.get("lead_id", None)
        if lead_id == None or lead_id == '':
            return fail("Lead id has not provided")
        try:
            leadObj = Leads.objects.get(id=lead_id)
        except Exception as e:
            return fail("Lead doesn't exist")
        isCommit = request.POST.get("isCommit", None)
        if isCommit:
            leadObj.isInterested = True
            leadObj.save()
            return success("Lead stored as committed")
        else: 
            leadObj.isInterested = False
            leadObj.save()
            return success("Lead stored as Not Committed")
    return fail("Error in request")


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

@csrf_exempt
def getContactedLeads(request):
    if request.method == "POST":
        print("------------------------------")
        leads = Leads.objects.all().filter(isContacted=True)
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

@csrf_exempt
def editLead(request):
    if request.method == "POST":
        timeNow = str(datetime.datetime.now())
        # Also require employee id to store along with remarks
        emp_id = request.POST.get("emp_id", None)

        leadID = request.POST.get("id", None)
        fname = request.POST.get("fname", None)
        lname = request.POST.get("lname", None)
        address = request.POST.get("address", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        alternatePhone = request.POST.get("alternatePhone", None)
        purchaseDate = request.POST.get("purchaseDate", None)
        pincode = request.POST.get("pincode", None)
        newComments = request.POST.get("comments", None)
        
        try:
            lead = Leads.objects.get(id = leadID)
        except Exception as e:
            print(e)
            return fail("Lead is not present in the db")

        if fname is not None:
            lead.fname = fname
        if lname is not None:
            lead.lname = lname
        if address is not None:
            lead.address = address
        if email is not None:
            lead.email = email
        if phone is not None:
            lead.phone = phone
        if alternatePhone is not None:
            lead.alternatePhone = alternatePhone
        if purchaseDate is not None:
            lead.purchaseDate = purchaseDate
        if pincode is not None:
            lead.pincode = pincode
        if comments is not None:
            # this part need to be fixed
            lead.comments = comments
            # oldComment = lead.comments
            # newComment = oldComment + "\n\n\n" + "----------------------------" + "\n" + \
            #     comments + "\n" + "----------------------------" + "\n" + timeNow + ' ' + emp_id
        lead.save()
        return success("Lead info updated")
    return fail("Error in request")


@csrf_exempt
def getSingleLead(request):
    if (request.method == "POST"):
        leadID = request.POST.get("id", None)
        try:
            leadObj = Leads.objects.get(id=leadID)
        except expression as identifier:
            return fail("Lead Not Found")
        lead = {}

        lead['id'] = leadObj.id
        lead['fname'] = leadObj.fname
        lead['lname'] = leadObj.lname
        lead['email'] = leadObj.email
        lead['mobile'] = leadObj.phone
        lead['alternatePhone'] = leadObj.alternatePhone
        lead['address'] = leadObj.address
        lead['purchaseDate'] = leadObj.purchaseDate
        lead['pincode'] = leadObj.pincode
        lead['comments'] = leadObj.comments

        return success(lead)
    return HttpResponse("Error In Request")


@csrf_exempt
def changeEmpPass(request):
    if request.method == "POST":
        emp_id = request.POST.get("id", None)
        newPassword = request.POST.get("newPassword", None)
        
        try:
            empObj = Employee.objects.get(id = emp_id)
        except Exception as e:
            print(e)
        empObj.password = newPassword
        empObj.save()
        return success("Password successfully changed.")
    return fail("Error in Request")


@csrf_exempt
def makeCall(request):
    if (request.method == "POST"):
        phone = request.POST.get("phone", None)
        # connect to vici dialler api


@csrf_exempt
def leadParser(request):
    if (request.method == "POST"):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = pd.read_excel(uploaded_file_url)
        row, col = data.shape
        rows = []
        for i in range(row):
            email, fname, lname, address, phone, alternatePhone, pincode, purchasedDate = data.loc[i,['email', 'fname', 'lname', 'address', 'phone', 'alternatePhone', 'pincode', 'purchasedDate']]
            lead = Leads(email=email, fname=fname, lname=lname, address=address, phone=phone, alternatePhone=alternatePhone, pincode=pincode, purchasedDate=purchasedDate)
            rows.append(lead)
        Leads.objects.bulk_create(
            rows
        )
        print(data)
        return success("completed upload")
    return fail("Error in request")

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

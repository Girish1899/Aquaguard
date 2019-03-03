from django.shortcuts import render,HttpResponse
from .models import Employee, Customers, Product, Complaints
# from .models import Employee,Customer,CurrentBooking,Product

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from .views import fail, success


# create a customer

# register a complaint
@csrf_exempt
def createComplaint(request):
    if(request.method=="POST"):
        custID = request.POST.get('id', None)
        try:
            custObj = Customers.objects.get(id=custID)
        except Exception as e:
            return fail("Customer doesn't exist")

        problem_description = request.POST.get('problem_description', None)
        severity = request.POST.get('severity', None)
        subject = request.POST.get('subject', None)
        if(problem_description==None and severity==None and subject==None):
            return fail("Invalid data")

        complaint = Complaints()
        complaint.problem_description = problem_description
        complaint.severity = severity
        complaint.subject = subject
        complaint.save()
        return success("Complaint has been saved")
    return fail("Error in request")





# register a complaint
# @csrf_exempt
# def createComplaint(request):
#     if(request.method=="POST"):
#         custID = request.POST.get('id', None)
#         try:
#             custObj = Customers.objects.get(id=custID)
#         except Exception as e:
#             return fail("Customer doesn't exist")

#         problem_description = request.POST.get('problem_description', None)
#         severity = request.POST.get('severity', None)
#         subject = request.POST.get('subject', None)
#         if(problem_description==None and severity==None and subject==None):
#             return fail("Invalid data")

#         complaint = Complaints()
#         complaint.problem_description = problem_description
#         complaint.severity = severity
#         complaint.subject = subject
#         complaint.save()
#         return success("Complaint has been saved")
#     return fail("Error in request")




# def displayAllTickets(request):
#     currentBooking=CurrentBooking.objects.all()
#     for i in range(len(currentBooking)):
#         ticket={}

@csrf_exempt
def checkPhone(request):
    if (request.method=="POST"):
        phone=request.POST.get('phone',None)
        print(phone)
        cust=Customers.objects.filter(mobile=phone)
        data={}
        print("this is the legnth",len(cust))
        if(len(cust) != 0):
            data['phone']=cust[0].mobile
            data['product_id']=cust[0].Equipment.product_id
            data['product_name']=cust[0].Equipment.name
            data['fname']=cust[0].fname
            data['lname']=cust[0].lname
            data['email']=cust[0].email
            data['alternativeMobile']=cust[0].alternativeMobile
            data['address']=cust[0].address
            data['pincode']=cust[0].pincode
            data['id']=cust[0].id

            return success(data)
        else:
            return fail("sorry no data found")

    else:
        return fail("please do make a post request")

@csrf_exempt
def checkMail(request):
    if (request.method=="POST"):
        mail=request.POST.get('mail',None)
        print(mail)
        cust=Customers.objects.filter(email=mail)
        data={}
        print("this is the legnth",len(cust))
        if(len(cust) != 0):
            data['phone']=cust[0].mobile
            data['product_id']=cust[0].Equipment.product_id
            data['product_name']=cust[0].Equipment.name
            data['fname']=cust[0].fname
            data['lname']=cust[0].lname
            data['email']=cust[0].email
            data['alternativeMobile']=cust[0].alternativeMobile
            data['address']=cust[0].address
            data['pincode']=cust[0].pincode
            data['land']=cust[0].land
            data['id']=cust[0].id

            return success(data)
        else:
            return fail("sorry no data found")

    else:
        return fail("please do make a post request")

# @csrf_exempt
# def existCustomerProblemRegistration(request):
#     if(request.method=="POST"):
#         print("hello")
#         #userRelated data
#         problem_description=request.POST.get('problem',None)
#         cid=request.POST.get('cid',None)
#         print("This is problem",problem_description)
#         print(problem_description)
#         if(problem_description==None and cid==None ):
#             return fail("Invalid data")
#         else:
#             # device problem registration
           
#             customer=Customer.objects.get(id=cid)

#             if (customer.id >= 0):
#                 ticket = CurrentBooking(problem_description=problem_description, customer=customer)
#                 ticket.save()
#                 ticket_details = {}
#                 ticket_details['ticket_id'] = ticket.bookingId
#                 ticket_details['resp'] = "New ticket raised"
#                 return success("ticke is hosted")
#     else:
#         return fail("post operation is required")

#     print("invalid page option")
#     return HttpResponse("Invalid page")


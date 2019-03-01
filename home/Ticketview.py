from django.shortcuts import render,HttpResponse
from .models import Employee, Customers, Product
# from .models import Employee,Customer,CurrentBooking,Product

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from .views import fail, success

# #REGISTER BOOKING
# @csrf_exempt
# def CustomerProblemRegistration(request):
#     if(request.method=="POST"):
#         print("hello")
#         #userRelated data
#         fname,lname,email=request.POST.get('fname',None),request.POST.get('lname',None),request.POST.get('email',None)
#         mobile,altermobile=request.POST.get("phone",None),request.POST.get('alter',None)
#         address,devicename,pincode=request.POST.get('address',None),request.POST.get('device',None),request.POST.get('pincode',None)
#         problem_description=request.POST.get('problem',None)
#         land=request.POST.get('land',None)
#         print(fname)
#         print(lname)
#         print(email)
#         print(mobile)
#         print(altermobile)
#         print(address)
#         print(devicename)
#         print(pincode)
#         print(problem_description)
#         if(fname==None and address==None and devicename==None and pincode==None and problem_description==None):
#             return fail("Invalid data")
#         else:
#             # device problem registration
#             prod=Product.objects.get(product_id=devicename)
#             print(prod)
#             print("creating customer")
#             customer = Customer(fname=fname, lname=lname, email=email, mobile=mobile,alternativeMobile=altermobile,address=address,pincode=pincode, Equipment=prod,isClient=True,land=land)
#             res=customer.save()
#             print(res)
#             print("customer created")
#             print(customer.id)

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


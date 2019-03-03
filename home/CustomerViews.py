from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
from .views import success,fail
from .models import Customers, Employee, Leads, EmpStatus, Product



@csrf_exempt
def addNewCustomer(request):
    if (request.method == "POST"):
        fname = request.POST.get("fname",None)
        lname = request.POST.get("lname",None)
        mobile = request.POST.get("mobile",None)
        email = request.POST.get("email",None)
        address = request.POST.get("address",None)
        pincode = request.POST.get("pincode",None)
        productID = request.POST.get("productID", None)
        alternativeMobile = request.POST.get("alternativeMobile",None)
        if (fname == None or lname ==  None or mobile ==  None or email ==  None or
                address ==  None or pincode ==  None or alternativeMobile ==  None):
           return fail("Invalid details")
        try:
            prodObj = Product.objects.get(id = productID)
        except Exception as e:
            return fail("Product doesn't exist")
        lead = Customers(fname = fname, lname = lname, mobile = mobile, email = email,
            address = address, pincode = pincode, alternativeMobile = alternativeMobile, product = prodObj)
        lead.save()
        return success("New Lead created!")
    return fail("Invalid Admin Page")


# @csrf_exempt
# def getSingleCustomer(request):
#     if (request.method=="POST"):
#         custID = request.POST.get("id",None)
#         custObj=Customers.objects.get(id = custID)
#         customer={}
#         customer['fname']=custObj.fname
#         customer['lname']=custObj.lname
#         customer['email']=custObj.email
#         customer['mobile']=custObj.phone
#         customer['alternativeMobile']=custObj.alternativeMobile
#         customer['address']=custObj.address
#         customer['pincode']=custObj.pincode
#         return success(customer)
#     return HttpResponse("Error In Request")
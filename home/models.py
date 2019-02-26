from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    empID = models.CharField(max_length=12, unique=True, default=None)
    phone = models.CharField(max_length=12, default=None)
    password = models.CharField(max_length=20, default='password')
    pincode = models.CharField(max_length=6, default="000000")
    email = models.CharField(max_length=30, default="None")
    type = models.CharField(max_length=2, default='tc')
    isActive = models.BooleanField(default=False)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    profilePicture = models.ImageField(null=True, upload_to="home/static/images/employee/")
#EMPLOYEE TYPE
#'tc'->tele caller 
#'tn'->technician
#'ts'->tech support
#'ad'->admin


class EmpStatus(models.Model):
    id = models.AutoField(primary_key=True)
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    loginTime = models.CharField(max_length=10, null=True)
    logoutTime = models.CharField(max_length=10, null=True)
    date = models.CharField(max_length=10, null=True)



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    product_id = models.CharField(max_length=30, unique=True)
    year = models.CharField(max_length=20)
    cost = models.IntegerField()
    category = models.CharField(max_length=2, default='mn')
    features = models.TextField(null=True)
#CATEGORIES
#'eq'-EQUIPMENT
#'mn'-MACHINE
#'fl'-FILTER


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    cust_ID = models.CharField(max_length=30, unique=True, default=None)
    fname = models.CharField(max_length=30, default=None)
    lname = models.CharField(max_length=20, default=None)
    email = models.CharField(max_length=30, default=None)
    mobile = models.CharField(max_length=12, default=None)
    alternativeMobile = models.CharField(max_length=12, default=None)
    address = models.CharField(max_length=300, default=None)
    pincode = models.CharField(max_length=6, default=None)




class Complaints(models.Model):
    id = models.AutoField(primary_key=True)
    req_id = models.CharField(max_length=30, default=None)
    subject = models.CharField(max_length=100)
    problem_description = models.TextField()
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL,null=True)
    technician = models.ForeignKey(Employee, on_delete=models.SET_NULL,null=True)
    request_date = models.DateField(auto_now_add=True)
    recording_data_url = models.TextField()
#INFO:
#req_id is same as booking_id


class Leads(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, default=None)
    lname = models.CharField(max_length=100, default=None)
    address = models.TextField(default=None, null=True)
    email = models.EmailField(default=None, null=True)
    phone = models.CharField(max_length=12, default=None, null=True)
    alternatePhone = models.CharField(max_length=12, default=None, null=True)
    purchaseDate = models.DateTimeField(auto_now_add=True)
    pincode = models.CharField(max_length=6, default="000000")
    comments = models.TextField(null=True)
    assignee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    isContacted = models.BooleanField(default=False)
    isInterested = models.BooleanField(default=False)


class CallData(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    leadID = models.ForeignKey(Leads, on_delete=models.SET_NULL, null=True)
    duration = models.DurationField()
    phone = models.CharField(max_length=12, default=None)
    remarks = models.TextField(default=None)
    recordLink = models.TextField()











# ------------------------------------------------------------------------- #


# All leads
#isContacted = na, yes, no
# class MyLeads(models.Model):
#     id = models.AutoField(primary_key=True)
#     fname = models.CharField(max_length=100)
#     lname = models.CharField(max_length=100)
#     address = models.TextField()
#     email = models.EmailField()
#     phone = models.IntegerField(default=None)
#     date = models.DateTimeField(auto_now_add=True)
#     pincode = models.CharField(max_length=6, default="000000")
#     isContacted = models.CharField(max_length=3,default='no')
#     isInterested = models.CharField(max_length=3,default='na')



#SEPERATE TABLE NEED TO BE DEVELOPED FOR CUSTOMER AND EQUIPMENT RELATION
#BECAUSE ONE CUSTOMER MAY HAVE MULTIPLE EQUIPMENT WITH HIM
#IN CASE THAT THE CUSTOMER IS NOT A CLIENT THE DEVICE WHICH HE ENQUIRED FOR IS PUT IN
# STATUS nyc->not_yet_called nas->not_answered crs->call_resheduled nin->not_intrested 
    # inr->intrested nav->not_available
#This table would contain inbound customer information.
# class Customer(models.Model):
#     id = models.AutoField(primary_key=True)
#     fname = models.CharField(max_length=30 , default=None)
#     lname = models.CharField(max_length=20, default=None)
#     email = models.CharField(max_length=30, default=None)
#     mobile = models.CharField(max_length=10, default=None)
#     alternativeMobile = models.CharField(max_length=10, default=None)
#     address = models.CharField(max_length=300, default=None)
#     pincode = models.CharField(max_length=6, default=None)
#     #DEVICE NAME
#     Equipment = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
#     isClient = models.BooleanField(default=False)
#     land = models.CharField(max_length=100, default=None)
#     comments = models.TextField(null=True)
#     status = models.CharField(max_length=10, default="nyc")
#     assign = models.BooleanField(default=False)



#THIS TABLE WOULD CONTAIN THE CONTACTED LEAD INFORMATION.
#Not response -> nr, Reschedule -> rs, NotInterested -> ni, Interested -> in, NotAvailable ->, NotCalled -> nc
# class ContactedLeads(models.Model):
#     id = models.AutoField(primary_key=True)
#     emp_id = models.ForeignKey(Employee, on_delete = models.SET_NULL, null=False)
#     email = models.EmailField()
#     mobile = models.IntegerField(max_length=10, default=None)
#     date = models.DateTimeField(auto_now_add=True)
#     pincode = models.CharField(max_length=6, default="000000")
#     category = models.CharField(max_length=2,default='mn')
#     status = models.CharField(max_length=2,default='nc')


#THIS DATA IS FETCHED FROM CURRENT BOOKING WHILE BOOKING IS EXECUTED
# class previousBooking(models.Model):
#     id = models.AutoField(primary_key=True)
#     bookingId=models.IntegerField()
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     technician = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     problem_description = models.TextField()
#     request_date = models.DateField()
#     recording_data_url = models.TextField()
#     completed_date = models.DateField(auto_now_add=True)


# class CallWorkLog(models.Model):
#     id = models.AutoField(primary_key=True)
#     telecaller = models.ForeignKey(Employee, on_delete=models.SET_NULL,null=True)
#     bookingId = models.IntegerField()



#status INprogress='ip'. and completed='cp'
# class CustomerEmployee(models.Model):
#     customer= models.ForeignKey(Customer, on_delete = models.SET_NULL,null=True)
#     employee= models.ForeignKey(Employee, on_delete = models.SET_NULL,null=True)
#     dateAssigned = models.DateField(auto_now_add = True)
#     status = models.CharField(max_length=15, default="ip")

#calls count per day
# class CallsPerDay(models.Model):
#     id = models.AutoField(primary_key=True)
#     dateAssigned = models.DateField(auto_now_add = True)
#     employee = models.ForeignKey(Employee, on_delete = models.SET_NULL,null=True)
#     totalCalls = models.IntegerField(default = 100)
#     completedCalls = models.IntegerField(default = 0)









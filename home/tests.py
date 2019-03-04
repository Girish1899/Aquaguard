from django.test import TestCase

# from .models import Employee,Customer,Product,CustomerEmployee, CallsPerDay, Leads
from .models import Employee, Customers, Product, Leads
# Create your tests here.

def fill_database_with_dummy_values():
    addEmployees()
    # addProducts()
    # addCustomers()
    # addDummyLeads()
    # addCustomerEmployeeRelation()

def cleanDatabase():
    Employee.objects.all().delete()
    Product.objects.all().delete()
    Customers.objects.all().delete()


def addEmployees():
    #     EMPLOYEE INSERTION PROCEDURE
    emp1 = Employee(empID=1000, phone='8483800288', password='password', pincode='560077', email='drake.penn@gmail.com', type='tn', fname='drake', lname='penn')
    emp1.save()

    emp2 = Employee(empID=1001, phone='8483800288', password='password', pincode='560077', email='bob.thomas@gmail.com', type='tc', fname='bob', lname='thomas')
    emp2.save()

    emp3 = Employee(empID=1002, phone='8483800288', password='password', pincode='560077', email='michale.john@gmail.com', type='tc', fname='michale', lname='john')
    emp3.save()

    emp4 = Employee(empID=1003, phone='8483800288', password='password', pincode='560077', email='fred.durst@gmail.com', type='ad', fname='fred', lname='durst')
    emp4.save()

    print("employees has been added")

# def addProducts():
#     #    PRODUCT TABLE INSERTION
#     product = Product(name="Aqua Phobia", description="Twin UI filter protection", product_id="AQUA2018PD011",
#                       cost=15000, year='2018', features='Anti bacteria resistal ions')
#     product.save()

#     product = Product(name="Aqua Fin", description="Multi heating level ", product_id="AQUA2017PD022",
#                       cost=13000,
#                       year='2017', features='Anti bacteria resistal ions')
#     product.save()
#     product = Product(name="Aqua milton", description="Twin UI filter protection", product_id="AQUA2018pd012",
#                       cost=5000,
#                       year='2003', features='Anti bacteria resistal ions')
#     product.save()

# def addCustomers():
#     cust=Customer(id=1000000 ,fname='Navya',lname="reddy",email='navya.reddy@gmail.com',phone='6361567775',pincode='560078',address='J.p nagar 1st phase'
#                   ,alternativephone='',land='Sindoor convention hall')
#     cust.save()
#     cust = Customer(fname='Guntur', lname="Shashi", email='guntur.shashi@gmail.com', phone='6361567773', pincode='560078',
#                     address='J.p nagar 1st phase'
#                     , alternativephone='',land='Bangalore central')
#     cust.save()
#     cust = Customer(fname='Salman', lname="khan", email='saleman.khan@gmail.com', phone='9008522228', pincode='560078',
#                     address='J.p nagar 1st phase'
#                     , alternativephone='',land="gopalan mall")
#     cust.save()

# def addCallsHistories(id):
#     calls = CallsPerDay(id = 1002, totalCalls = 50, completedCalls = 40)


# def addCustomerEmployeeRelation():
#     ce=CustomerEmployee(customer=Customer.objects.get(fname='Navya', lname='reddy'),employee=Employee.objects.get(phone='8686168832'))
#     ce.save()
#     ce = CustomerEmployee(customer=Customer.objects.get(fname='Guntur', lname='Shashi'),
#                           employee=Employee.objects.get(phone='8686168832'))
#     ce.save()



# def displayLeads(id):
#     emp=Employee.objects.get(id=id)
#     ce=CustomerEmployee.objects.filter(employee=emp)
#     for row in ce:
#         print(row.employee.name+"-->"+row.customer.fname)




def addDummyLeads():
    #     This function add dummy leads
    
    emp1 = Leads(fname='Matilde', lname='Tym', address='5460 Morningstar Drive', email='frew0@smh.com.au', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp1.save()

    emp2 = Leads(fname='Averill', lname='Mather', address='4 Vidon Lane', email='amather1@networkadvertising.org', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp2.save()

    emp3 = Leads(fname='Rad', lname='TymLidgerton', address='7 Badeau Parkway', email='rlidgerton2@issuu.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp3.save()

    emp4 = Leads(fname='Chrystel', lname='Saunier', address='7 Hooker Park', email='csaunier3@livejournal.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp4.save()

    emp5 = Leads(fname='Matilde', lname='Tym', address='33572 Coleman Park', email='bbaudinot4@i2i.jp', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp5.save()

    emp6 = Leads(fname='Barrie', lname='Baudinot', address='19 Esch Center', email='mpagett5@nature.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp6.save()

    emp7 = Leads(fname='Mercedes', lname='Pagett', address='6 Browning Lane', email='cmorilla6@dropbox.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp7.save()

    emp8 = Leads(fname='Clemmie', lname='Morilla', address='0 Harper Crossing', email='eborghese7@goodreads.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp8.save()

    emp9 = Leads(fname='Elmore', lname='Borghese', address='3330 Tomscot Point', email='tjills8@skype.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp9.save()

    emp10 = Leads(fname='Tedmund', lname='Jills', address='77 Sutteridge Crossing', email='ilagden9@friendfeed.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp10.save()

    emp11 = Leads(fname='Iosep', lname='Lagden', address='	37 Fisk Avenue', email='ffraina@indiatimes.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp11.save()

    emp12 = Leads(fname='Floyd', lname='Frain', address='392 Grim Trail', email='kkilkennyb@reverbnation.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp12.save()

    emp13 = Leads(fname='Krisha', lname='Kilkenny', address='65 Memorial Trail', email='ajacmardc@issuu.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp13.save()

    emp14 = Leads(fname='Arluene', lname='Jacmard', address='02852 Annamark Trail', email='atoore@feedburner.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp14.save()

    emp15 = Leads(fname='Alexa', lname='Kedie', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp15.save()

    emp16 = Leads(fname='Adele', lname='McClaurie', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050')
    emp16.save()

    emp17 = Leads(fname='Jill', lname='Croux', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp17.save()

    emp18 = Leads(fname='Rodie', lname='Orans', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp18.save()

    emp19 = Leads(fname='Conney', lname='Coggill', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp19.save()

    emp20 = Leads(fname='Caroline', lname='Joutapavicius', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp20.save()

    emp21 = Leads(fname='Ase', lname='Helix', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isInterested=False, isContacted=True)
    emp21.save()

    emp22 = Leads(fname='Florian', lname='Lemery', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isInterested=False, isContacted=True)
    emp22.save()

    emp23 = Leads(fname='Barbra', lname='Clissol', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp23.save()

    emp24 = Leads(fname='Koral', lname='Snelling', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp24.save()

    emp25 = Leads(fname='Sadella', lname='Ewbanke', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp25.save()

    emp26 = Leads(fname='Johannah', lname='Revey', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp26.save()

    emp27 = Leads(fname='Sissy', lname='MacFadden', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9836837893', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp27.save()

    print("Dummy leads saved")



def addProduct():
    product=Product(name="filter",description="for filtering water",builtYear="2019",cost=3000,category="sp")
    product.save()
    product=Product(name="purifier",description="for filtering water",builtYear="2019",cost=3000,category="sp")
    product.save()
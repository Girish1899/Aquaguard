"""aquaguard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import login,registration
from .EmployeeView import uploadEmployeeProfilePic
from .ProductViews import createNewDevice,displayAllDevice,deleteDevice
# from .adminViews import addNewLead, displayAssignedLeads, displaySingleLead, updateStatus,empLogin,getCallCount,setCallCount, loginPage, homePage, getSession

from .adminViews import empLoginCheck, getSession, getAssignedLeads, getUserData, storeSession, flushSession, getInterestedLeads, getLeadsNotContacted, storeLogoutTime
from .adminViews import loginPage, homePage, logoutPage, homePageCommittedLeads, homePageContactLeads, changedp
# from .EmployeeView import createNewEmployee,displayAllEmployee,deactivateEmployee
# from .Ticketview import CustomerProblemRegistration,displayAllTickets,checkPhone,checkMail,existCustomerProblemRegistration

urlpatterns = [
    # path("registerEmployee/",createNewEmployee),
    # path("displayEmployee/",displayAllEmployee),
    # path("deactivateEmployee/",deactivateEmployee),
    # path("updateStatus/",updateStatus),
    # path("getCallCount/",getCallCount),
    # path("setCallCount/",setCallCount),
    # path("displaySingleLead/",displaySingleLead),
    # path("registerTicketExist/",existCustomerProblemRegistration),
    # path("registerTicket/",CustomerProblemRegistration),
    # path("checkPhone/",checkPhone),
    # path("checkMail/",checkMail),
    # path("addNewLead/",addNewLead),
    path("loginTechnician/", login),
    path("registerTechnician/", registration),
    path("addNewProduct/", createNewDevice),
    path("displayAllDevice/", displayAllDevice),
    path("deleteDevice/", deleteDevice),
    path("getAssignedLeads/", getAssignedLeads),
    path("getInterestedLeads/", getInterestedLeads),
    path("getLeadsNotContacted/", getLeadsNotContacted),
    path("getUserData/", getUserData),
    path("getSession/", getSession),
    path("storeSession/", storeSession),
    path("flushSession/", flushSession),
    path("empLoginCheck/", empLoginCheck),
    path("storeLogoutTime/", storeLogoutTime),
    path("addProfilePic/", uploadEmployeeProfilePic),
#----------------------------------------------#
    path("", loginPage),
    path("homePage/", homePage),
    path("homePageCommittedLeads/", homePageCommittedLeads),
    path("homePageContactLeads/", homePageContactLeads),
    path("changedp/", changedp),
    path("logoutPage/", logoutPage)
]

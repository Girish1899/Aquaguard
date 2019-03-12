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
from .EmployeeView import updateEmployee,uploadEmployeeProfilePic
# from .ProductViews import deleteDevice,getProductDetails
# from .adminViews import addNewLead, displayAssignedLeads, displaySingleLead, updateStatus,empLogin,getCallCount,setCallCount, loginPage, homePage, getSession


from .adminViews import empLoginCheck, getSession, getAssignedLeads, getUserData, storeSession, flushSession, getInterestedLeads,getSingleLead, getLeadsNotContacted, storeLogoutTime, makeCall, addProfilePicture, getProfilePicture, setCommit,editLead, togglePause, getContactedLeads
from .adminViews import loginPage, homePage, logoutPage, homePageCommittedLeads, homePageContactLeads, changedp, forgotPassword, callHistoryPage, commitHistoryPage

from .adminViews import empLoginCheck, getSession, getAssignedLeads, getUserData, storeSession, flushSession, getInterestedLeads, getLeadsNotContacted, storeLogoutTime, makeCall
from .adminViews import loginPage, homePage, logoutPage, homePageCommittedLeads, homePageContactLeads, changedp, forgotPassword
from .adminViews import addProfilePicture, getProfilePicture, setNotification, getNotification

# from .EmployeeView import createNewEmployee,displayAllEmployee,deactivateEmployee
# from .Ticketview import CustomerProblemRegistration,displayAllTickets,checkPhone,checkMail,existCustomerProblemRegistration

urlpatterns = [
    # path("registerEmployee/",createNewEmployee),
    # path("displayEmployee/",displayAllEmployee),
    # path("deactivateEmployee/",deactivateEmployee),
    # path("updateStatus/",updateStatus),
    # path("getCallCount/",getCallCount),
    # path("setCallCount/",setCallCount),
    path("editLead/", editLead),
    path("displaySingleLead/", getSingleLead),
    # path("registerTicketExist/",existCustomerProblemRegistration),
    # path("registerTicket/",CustomerProblemRegistration),
    # path("checkPhone/",checkPhone),
    # path("checkMail/",checkMail),
    # path("addNewLead/",addNewLead),
    path("loginTechnician/", login),
    path("registerTechnician/", registration),
    # path("addNewProduct/", createNewDevice),
    # path("displayAllDevice/", displayAllDevice),
    # path("deleteDevice/", deleteDevice),
    path("changedp/", changedp),
    path("getAssignedLeads/", getAssignedLeads), 
    path("getInterestedLeads/", getInterestedLeads),
    path("getLeadsNotContacted/", getLeadsNotContacted),
    path("getContactedLeads/", getContactedLeads),
    path("getUserData/", getUserData),
    path("getSession/", getSession),
    path("storeSession/", storeSession),
    path("flushSession/", flushSession),
    path("empLoginCheck/", empLoginCheck),
    path("storeLogoutTime/", storeLogoutTime),
    path("addProfilePic/", uploadEmployeeProfilePic),
    path("makeCall/", makeCall),
    path("addProfilePicture/", addProfilePicture),
    path("getProfilePicture/", getProfilePicture),
    path("setNotification/", setNotification),
    path("getNotification/", getNotification),
    path("setCommit/", setCommit),
    path("setPause/", togglePause),
#----------------------------------------------#
    path("", loginPage),
    path("homePage/", homePage),
    path("homePageCommittedLeads/", homePageCommittedLeads),
    path("homePageContactLeads/", homePageContactLeads),
    path("callHistoryPage/", callHistoryPage),
    path("commitHistoryPage/", commitHistoryPage),
    path("changedp/", changedp),
    path("forgotPassword/", forgotPassword),
    path("logoutPage/", logoutPage),

#-------------changes by rahul -----------------#
    path("updateEmployee/", updateEmployee),
    # path("getProductDetail/",getProductDetails),

]

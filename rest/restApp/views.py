from django.shortcuts import render
from restApp.models import *
from django.http import HttpResponse
SUCCESSFUL_LOGIN = "11"
UNSECCESSFUL_LOGIN = "00"

def weatherAppLogIn(request):
    requestUsername = request.GET.getlist("username")[0]
    requestPassword = request.GET.getlist("password")[0]
    queryRes = User.objects.filter(user_name=requestUsername)
    response = HttpResponse(content_type="text/plain")
    response["Content-Type"] = "text/plain"
    exist = False
    for i in queryRes:
        if i.user_name == requestUsername and i.password == requestPassword:
            exist = True
    if exist:
        response.write(SUCCESSFUL_LOGIN)
    else:
        response.write(UNSECCESSFUL_LOGIN)

    return response
def createRoot(request):
    ROOT_UNAME = 'root'
    ROOT_PASS = 'root'
    queryRes = User.objects.filter(user_name=ROOT_UNAME)
    rootFound = False
    for i in queryRes:
        if i.user_name == ROOT_UNAME:
            rootFound = True
    if rootFound:
        return HttpResponse("Root already exist",content_type="text/plain")
    else:
        root = User.objects.create(user_name=ROOT_UNAME,password=ROOT_PASS)
        root.save()
        return HttpResponse("Root has been saved!",content_type="text/plain")
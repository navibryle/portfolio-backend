from django.shortcuts import render
from restApp.models import *
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django_ap.models import UseName
from django_ap.models import AccessData
from django_ap.models import DoneData
from datetime import datetime
from django.core import serializers

SUCCESSFUL_LOGIN = "11"
UNSECCESSFUL_LOGIN = "00"

ACCOUNT_CREATED = "22"
ACCOUNT_EXSIST = "33"

SUCCESSFUL_CREATTION = "77"

SUCCESSFULY_SAVED = "91"
UNSECCESSFUL_SAVE = "92"

SUCCESSFULY_DELETED = "92"
UNSUCCESSFULY_DELETED = "92"
def weatherAppLogIn(request):
    requestUsername = request.GET.getlist("username")[0]
    requestPassword = request.GET.getlist("password")[0]
    queryRes = User.objects.filter(user_name=requestUsername)
    response = HttpResponse(content_type="text/plain")
    response['Access-Control-Allow-Origin'] = '*'
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
@csrf_exempt
def createUser(request):
    requestUsername = request.GET.getlist("username")[0]
    requestPassword = request.GET.getlist("password")[0]
    queryRes = User.objects.filter(user_name=requestUsername)
    if len(queryRes) > 0:
        resp = HttpResponse(ACCOUNT_EXSIST,content_type="text/plain")
        return resp
    else:
        user = User(user_name=requestUsername,password=requestPassword)
        user.save()
        resp = HttpResponse(ACCOUNT_CREATED,content_type="text/plain")
        return resp

@csrf_exempt
def saveCities(request):
    requestUsername = request.GET.getlist("username")[0]
    requestDataset = request.GET.getlist("dataset")[0]
    user = User.objects.filter(user_name=requestUsername)[0]
    dataset = Datasets.objects.filter(user_name = user,dataset_name = requestDataset)[0]
    reqBody = json.loads(request.body)
    saved = 0
    for i in reqBody:
        data = WeatherDataset(
            user_name = user,
            dataset_name = dataset,
            name = reqBody[i]['name'],
            temp = reqBody[i]['temp'],
            feels_like = reqBody[i]['feels_like'],
            temp_min = reqBody[i]['temp_min'],
            temp_max = reqBody[i]['temp_max'],
            pressure = reqBody[i]['pressure'],
            humidity = reqBody[i]['humidity'],
            visibility = reqBody[i]['visibility'],
            iconUrl = reqBody[i]['iconUrl'],
            description = reqBody[i]['description']
            )
        if not WeatherDataset.objects.filter(
            user_name = user,
            dataset_name = dataset,
            name = reqBody[i]['name'],
            temp = reqBody[i]['temp'],
            feels_like = reqBody[i]['feels_like'],
            temp_min = reqBody[i]['temp_min'],
            temp_max = reqBody[i]['temp_max'],
            pressure = reqBody[i]['pressure'],
            humidity = reqBody[i]['humidity'],
            visibility = reqBody[i]['visibility'],
            iconUrl = reqBody[i]['iconUrl'],
            description = reqBody[i]['description']):
            data.save()
            saved += 1
    print(saved,len(reqBody))
    if saved == len(reqBody):
        #if all the rows got saved successful return
        return HttpResponse(SUCCESSFULY_SAVED,content_type="text/plain")
    return HttpResponse(UNSECCESSFUL_LOGIN,content_type="text/plain")
@csrf_exempt
def deleteCities(request):
    requestUsername = request.GET.getlist("username")[0]
    requestDatasetName = request.GET.getlist("dataset")[0]
    user = User.objects.filter(user_name=requestUsername)[0]
    dataset = Datasets.objects.filter(dataset_name=requestDatasetName,user_name=user)[0]
    datasets = WeatherDataset.objects.filter(user_name=user,dataset_name=dataset)
    datasets.delete()
    if datasets in WeatherDataset.objects.all():
        return HttpResponse(UNSUCCESSFULY_DELETED,content_type="text/plain")
    return HttpResponse(SUCCESSFULY_DELETED,content_type="text/plain")
def getTable(request):
    requestUsername = request.GET.getlist("username")[0]
    requestDatasetName = request.GET.getlist("dataset")[0]
    user = User.objects.filter(user_name=requestUsername)[0]
    dataset = Datasets.objects.filter(dataset_name=requestDatasetName,user_name=user)[0]
    tables = WeatherDataset.objects.filter(user_name=user,dataset_name=dataset)
    output = {}
    for i in tables:
        temp = {}
        temp['temp'] = i.temp
        temp['feels_like'] = i.feels_like
        temp['temp_min'] = i.temp_min
        temp['temp_max'] = i.temp_max
        temp['pressure'] = i.pressure
        temp['humidity'] = i.humidity
        temp['visibility'] = i.visibility
        temp['iconUrl'] = i.iconUrl
        temp['description'] = i.description
        output[i.name] = temp
    print(output)
    return JsonResponse(output)
def getDatasets(request):
    requestUsername = request.GET.getlist("username")[0]
    dataset = Datasets.objects.filter(user_name=requestUsername)
    output = {}
    for i in dataset:
        output[i.dataset_name] = i.dataset_name
    return JsonResponse(output)
def storeDataset(request):
    requestUsername = request.GET.getlist("username")[0]
    requestDataset = request.GET.getlist("dataset")[0]
    user = User.objects.filter(user_name=requestUsername)[0]
    newDataset = Datasets(user_name=user,dataset_name=requestDataset)
    if not Datasets.objects.filter(user_name=user,dataset_name=requestDataset):
        newDataset.save()
    return HttpResponse(SUCCESSFUL_CREATTION,content_type="text/plain")


#============================new api====================

def index(request):
    try:
        var = request.GET.get('UserName')
        pas = request.GET.get('pass')
        result = UseName.objects.get(user_Name=var, pas=pas)
        dic = {}
        dic['userName'] = result.user_Name
        dic['password'] = result.pas
        return JsonResponse(dic)
    except UseName.DoesNotExist:
        return HttpResponse(69)

@csrf_exempt
def createUser(request):
    name = request.GET.get('UserName')
    password = request.GET.get('pass')
    u = UseName(user_Name=name, pas=password)
    u.save()
    return HttpResponse(95)


@csrf_exempt
def get_items(request):
    try:
        name = request.GET.get('UserName')
        a = AccessData.objects.filter(user=name)
        data = {}
        for values in a:
            data['name'] = values.user
            data['habbit'] = values.item
            data['date'] = values.date
            data['endDate'] = values.endDate
  
        return JsonResponse(data)
    except AccessData.DoesNotExist:
        return HttpResponse(29)
        


@csrf_exempt
def add_items(request):
    name = request.GET.get('UserName')
    habbit = request.GET.get('habbit')
    d = datetime.now()
    a = AccessData(user=name, item=habbit, date=d, endDate=d)
    a.save()
    print(d)
    return HttpResponse(25)

@csrf_exempt
def doneItems(request):
    name = request.GET.get('name')
    doneHabbit = request.GET.get('habbit')
    dataHabbit = AccessData.objects.get(user=name, item=doneHabbit)
    dataHabbit.delete()
    id = 2
    id = id + 1
    d = datetime.now()
    result = DoneData(id, name, doneHabbit, d)
    result.save()
    print(result)
    return HttpResponse(2)

@csrf_exempt
def getDoneItems(request):
     try:
        name = request.GET.get('name')
        a = DoneData.objects.filter(user=name)
        data = {}
        for values in a:
            data['name'] = values.user
            data['item'] = values.item
            data['date'] = str(values.dateEnded)
        dumps = json.dumps(data)
        return JsonResponse(dumps, safe=False)
     except DoneData.DoesNotExist:
        return HttpResponse(39)
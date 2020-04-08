import pymysql
from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
import json
import requests



# Create your views here.

def index(request):
    return render(request,'index.html')

def luolidia(request):
    dia=''
    dialog=[]

    if request.method == 'POST':
        dia=request.POST.get('dialogue')
        dialog.append(dia)

        url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(dia)
        res = requests.get(url)
        res1 = json.loads(res.text)
        res2=res1['content'].replace('{br}', '\n').replace('菲菲','小萝莉').replace('晨风机器人','小萝莉')
        dialog.append(res2)
    return render(request,'luolidia.html',{'data':dialog})

def zyddia(request):
    dia=''
    dialog=[]

    if request.method == 'POST':
        dia=request.POST.get('dialogue')
        dialog.append(dia)

        url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(dia)
        res = requests.get(url)
        res1 = json.loads(res.text)
        res2=res1['content'].replace('{br}', '\n').replace('菲菲','zyd').replace('晨风机器人','沙雕zyd')
        dialog.append(res2)
    return render(request,'zyddia.html',{'data':dialog})






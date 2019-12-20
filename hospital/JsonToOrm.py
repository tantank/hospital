import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hospital.settings")

import django
django.setup()

import json
import numpy as np
from show.models import City,Hospital강원,Hospital경기,Hospital경남,Hospital경북,Hospital광주,Hospital대구,Hospital대전
from show.models import Hospital부산,Hospital서울,Hospital세종시,Hospital울산,Hospital인천,Hospital전남,Hospital전북,Hospital충남,Hospital충북


hospital = []
with open("../crawling/hospital_23000.json", "r") as json_file:
    st_python = json.load(json_file)
    hospital.append(st_python)

hospital = np.ravel(hospital,order='C')

print(hospital[1000]['yadmnm'])

city_list = City.objects.order_by('name')
print(city_list[1])
count = len(hospital)
print(count)

list = []

i = 0
while i < len(city_list):
    list.append(city_list[i].name)
    i=i+1
print(list)
print(list.index('경기'))
i = 0

print(hospital[i]['sidocdnm'])

def func강원(hos):
    Hospital강원(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func경기(hos):
    Hospital경기(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func경남(hos):
    Hospital경남(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func경북(hos):
    Hospital경북(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func광주(hos):
    Hospital광주(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func대구(hos):
    Hospital대구(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func대전(hos):
    Hospital대전(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func부산(hos):
    Hospital부산(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func서울(hos):
    Hospital서울(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func세종시(hos):
    Hospital세종시(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func울산(hos):
    Hospital울산(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func인천(hos):
    Hospital인천(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func전남(hos):
    Hospital전남(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func전북(hos):
    Hospital전북(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func충남(hos):
    Hospital충남(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()
def func충북(hos):
    Hospital충북(sidocdnm=hos['sidocdnm'],sggucdnm=hos['sggucdnm'],yadmnm=hos['yadmnm'],clcdnm=hos['clcdnm'],npaykornm=hos['npaykornm'],maxprc=hos['maxprc'],minprc=hos['minprc'],url=hos['url'],date=hos['date']).save()

def f(x,hos):
    return {
        '강원': lambda: func강원(hos),
        '경기': lambda: func경기(hos),
        '경남': lambda: func경남(hos),
        '경북': lambda: func경북(hos),
        '광주': lambda: func광주(hos),
        '대구': lambda: func대구(hos),
        '대전': lambda: func대전(hos),
        '부산': lambda: func부산(hos),
        '서울': lambda: func서울(hos),
        '세종시': lambda: func세종시(hos),
        '울산': lambda: func울산(hos),
        '인천': lambda: func인천(hos),
        '전남': lambda: func전남(hos),
        '전북': lambda: func전북(hos),
        '충남': lambda: func충남(hos),
        '충북': lambda: func충북(hos),
    }.get(x)()

#!@#!@#!@#!@$#%$@#$%$@#%@#$%@#%@#$%@#$%@#%$@#4   여기
while i < count:
    sido = hospital[i]['sidocdnm']
    f(sido,hospital[i])
    i=i+1

def delete_all_Object():
    Hospital강원.objects.all().delete()
    Hospital경기.objects.all().delete()
    Hospital경남.objects.all().delete()
    Hospital경북.objects.all().delete()
    Hospital광주.objects.all().delete()
    Hospital대구.objects.all().delete()
    Hospital대전.objects.all().delete()
    Hospital부산.objects.all().delete()
    Hospital서울.objects.all().delete()
    Hospital세종시.objects.all().delete()
    Hospital울산.objects.all().delete()
    Hospital인천.objects.all().delete()
    Hospital전남.objects.all().delete()
    Hospital전북.objects.all().delete()
    Hospital충남.objects.all().delete()
    Hospital충북.objects.all().delete()

#delete_all_Object()


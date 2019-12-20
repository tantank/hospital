from django.shortcuts import render
from . models import City,Hospital강원,Hospital경기,Hospital경남,Hospital경북,Hospital광주,Hospital대구,Hospital대전
from . models import Hospital부산,Hospital서울,Hospital세종시,Hospital울산,Hospital인천,Hospital전남,Hospital전북,Hospital충남,Hospital충북
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def index(request):
    city_list = City.objects.all()
    context = {'city_list':city_list}
    return render(request, 'home.html',context)
def show_list(request,city_name):
    city = get_object_or_404(City, name=city_name)

    def city_select(city_name):
        return {
            '강원': lambda: Hospital강원.objects.all().order_by('npaykornm'),
            '경기': lambda: Hospital경기.objects.all().order_by('npaykornm'),
            '경남': lambda: Hospital경남.objects.all().order_by('npaykornm'),
            '경북': lambda: Hospital경북.objects.all().order_by('npaykornm'),
            '광주': lambda: Hospital광주.objects.all().order_by('npaykornm'),
            '대구': lambda: Hospital대구.objects.all().order_by('npaykornm'),
            '대전': lambda: Hospital대전.objects.all().order_by('npaykornm'),
            '부산': lambda: Hospital부산.objects.all().order_by('npaykornm'),
            '서울': lambda: Hospital서울.objects.all().order_by('npaykornm'),
            '세종시': lambda: Hospital세종시.objects.all().order_by('npaykornm'),
            '울산': lambda: Hospital울산.objects.all().order_by('npaykornm'),
            '인천': lambda: Hospital인천.objects.all().order_by('npaykornm'),
            '전남': lambda: Hospital전남.objects.all().order_by('npaykornm'),
            '전북': lambda: Hospital전북.objects.all().order_by('npaykornm'),
            '충남': lambda: Hospital충남.objects.all().order_by('npaykornm'),
            '충북': lambda: Hospital충북.objects.all().order_by('npaykornm'),
        }.get(city_name)()

    data = city_select(city_name)
    page = request.GET.get('page',1)
    paginator = Paginator(data,20)
    try:
        hospitals = paginator.page(page)
    except PageNotAnInteger:
        hospitals = paginator.page(1)
    except EmptyPage:
        hospitals = paginator.page(paginator.num_pages)

    index = hospitals.number-1
    max_index = len(paginator.page_range)
    start_index = index-2 if index >= 2 else 0
    if index < 2:
        end_index = 5-start_index
    else:
        end_index = index+3 if index<=max_index-3 else max_index
    page_range=list(paginator.page_range[start_index:end_index])

    city_list = City.objects.all()
    context = {'city_list':city_list, 'hospitals':hospitals,'page_range':page_range,'max_index':max_index-2}
    return render(request, 'city.html',context)

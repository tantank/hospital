from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('select/<str:city_name>', views.show_list, name = 'show_list')

]
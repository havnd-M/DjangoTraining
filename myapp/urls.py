from ipaddress import ip_address
from django.urls import path
from myapp import views

urlpatterns = [

    path('home/', views.home),
    path('about/', views.about),
    path('connection/', views.connection),
    path('myip/', views.what_is_myip),
    path('', views.Home)

]

"""TMProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from TMTsys import views
from django.urls import re_path as url	

urlpatterns = [
    
    url(r'^adduser/$', views.addUser, name='adduser/'),
    url(r'^(\d+)/$', views.showUser, name='showuser/'),
    url(r'^(\d+)/showUser/', views.showUser, name='showUser'),
    path('checkout1/', views.checkout1, name='checkout1/'),
    url(r'^checkout2/(\d+)/$', views.checkout2, name='checkout2'),
    url(r'^checkout3/(\d+)/(\d+)/$', views.checkout3, name='checkout3'),
    url(r'^checkout4/(\d+)/$', views.checkout4, name='checkout4'),
    url(r'^delete/(\d+)/(\d+)/$', views.delete, name='delete'),
    url(r'^edit/(\d+)/(\d+)/$', views.editInfo, name='edit'),
    url(r'^update/(\d+)/(\d+)/$', views.updateInfo, name='update'),

    # url(r'^(\d+)/showuserpage/', views.showUserPage, name='showuserpage/'),
    # url(r'^(\d+)/adduser/', views.addUser, name='adduser/'),


    # url(r'^(\d+)/GadgetPage/', views.GadgetPage, name='GadgetPage'),
    #url(r'^(\d+)/CheckoutPage/', views.CheckoutPage, name='CheckoutPage'),
    # url(r'^(\d+)/Review/', views.Review, name='Review'),
    # url(r'^None/Review/', views.Review2, name='Review2'),
    # url(r'^edit/(\d+)', views.edit, name='edit'),
    # url(r'^edit/update/(\d+)', views.update, name='update'),
    # url(r'^(\d+)/delete/', views.delete, name='delete'),
    

    # navigation
    path('', views.homepage, name='homepage/'),
    
    path('laptop/', views.laptop, name='laptop/'),
    path('monitor/', views.monitor, name='monitor/'),
    path('mouse/', views.mouse, name='mouse/'),
    path('keyboard/', views.keyboard, name='keyboard/'),
    
    # path('checkout2/', views.checkout2, name='checkout2/'),
    path('checkout3/', views.checkout3, name='checkout3/'),
    path('checkout4/', views.checkout4, name='checkout4/'),
    path('checkout5/', views.checkout5, name='checkout5/'),
    path('contact/', views.contact, name='contact/'),
    path('feedback/', views.feedback, name='feedback/'),


    # SORTING
    path('laptopAsus/', views.laptopAsus, name='laptopAsus/'),
    path('laptopLenovo/', views.laptopLenovo, name='laptopLenovo/'),
    path('laptopDell/', views.laptopDell, name='laptopDell/'),

    path('monitorNVision/', views.monitorNVision, name='monitorNVision/'),
    path('monitorAsus/', views.monitorAsus, name='monitorAsus/'),
    path('monitorAcer/', views.monitorAcer, name='monitorAcer/'),

    path('mouseRazer/', views.mouseRazer, name='mouseRazer/'),
    path('mouseLogitech/', views.mouseLogitech, name='mouseLogitech/'),
    path('mouseSteel/', views.mouseSteel, name='mouseSteel/'),

    path('keyboardLogitech/', views.keyboardLogitech, name='keyboardLogitech/'),
    path('keyboardRazer/', views.keyboardRazer, name='keyboardRazer/'),
    path('keyboardCorsair/', views.keyboardCorsair, name='keyboardCorsair/'),


    # LAPTOPS

    # ASUS LAPTOPS
    path('asusL1/', views.asusL1, name='asusL1/'),
    path('asusL2/', views.asusL2, name='asusL2/'),
    path('asusL3/', views.asusL3, name='asusL3/'),
    path('asusL4/', views.asusL4, name='asusL4/'),
    path('asusL5/', views.asusL5, name='asusL5/'),

    # LENOVO LAPTOPS
    path('lenovoL1/', views.lenovoL1, name='lenovoL1/'),
    path('lenovoL2/', views.lenovoL2, name='lenovoL2/'),
    path('lenovoL3/', views.lenovoL3, name='lenovoL3/'),
    path('lenovoL4/', views.lenovoL4, name='lenovoL4/'),
    path('lenovoL5/', views.lenovoL5, name='lenovoL5/'),

    # DELL LAPTOPS
    path('dellL1/', views.dellL1, name='dellL1/'),
    path('dellL2/', views.dellL2, name='dellL2/'),
    path('dellL3/', views.dellL3, name='dellL3/'),
    path('dellL4/', views.dellL4, name='dellL4/'),
    path('dellL5/', views.dellL5, name='dellL5/'),



    # MONITORS

    # NVISION MONITORS
    path('nvisionMON1/', views.nvisionMON1, name='nvisionMON1/'),
    path('nvisionMON2/', views.nvisionMON2, name='nvisionMON2/'),
    path('nvisionMON3/', views.nvisionMON3, name='nvisionMON3/'),
    path('nvisionMON4/', views.nvisionMON4, name='nvisionMON4/'),
    path('nvisionMON5/', views.nvisionMON5, name='nvisionMON5/'),

    # ASUS MONITORS
    path('asusMON1/', views.asusMON1, name='asusMON1/'),
    path('asusMON2/', views.asusMON2, name='asusMON2/'),
    path('asusMON3/', views.asusMON3, name='asusMON3/'),
    path('asusMON4/', views.asusMON4, name='asusMON4/'),
    path('asusMON5/', views.asusMON5, name='asusMON5/'),

    # ACER MONITORS
    path('acerMON1/', views.acerMON1, name='acerMON1/'),
    path('acerMON2/', views.acerMON2, name='acerMON2/'),
    path('acerMON3/', views.acerMON3, name='acerMON3/'),
    path('acerMON4/', views.acerMON4, name='acerMON4/'),
    path('acerMON5/', views.acerMON5, name='acerMON5/'),    


    # MOUSE

    # RAZER MOUSE
    path('razerMOU1/', views.razerMOU1, name='razerMOU1/'),
    path('razerMOU2/', views.razerMOU2, name='razerMOU2/'),
    path('razerMOU3/', views.razerMOU3, name='razerMOU3/'),
    path('razerMOU4/', views.razerMOU4, name='razerMOU4/'),
    path('razerMOU5/', views.razerMOU5, name='razerMOU5/'),

    # LOGITECH MOUSE
    path('logiMOU1/', views.logiMOU1, name='logiMOU1/'),
    path('logiMOU2/', views.logiMOU2, name='logiMOU2/'),
    path('logiMOU3/', views.logiMOU3, name='logiMOU3/'),
    path('logiMOU4/', views.logiMOU4, name='logiMOU4/'),
    path('logiMOU5/', views.logiMOU5, name='logiMOU5/'),

    # STEELSERIES MOUSE
    path('steelMOU1/', views.steelMOU1, name='steelMOU1/'),
    path('steelMOU2/', views.steelMOU2, name='steelMOU2/'),
    path('steelMOU3/', views.steelMOU3, name='steelMOU3/'),
    path('steelMOU4/', views.steelMOU4, name='steelMOU4/'),
    path('steelMOU5/', views.steelMOU5, name='steelMOU5/'),


    # KEYBOARD

    # LOGITECH KEYBOARD
    path('logiKEY1/', views.logiKEY1, name='logiKEY1/'),
    path('logiKEY2/', views.logiKEY2, name='logiKEY2/'),
    path('logiKEY3/', views.logiKEY3, name='logiKEY3/'),
    path('logiKEY4/', views.logiKEY4, name='logiKEY4/'),
    path('logiKEY5/', views.logiKEY5, name='logiKEY5/'),

    # RAZER KEYBOARD
    path('razerKEY1/', views.razerKEY1, name='razerKEY1/'),
    path('razerKEY2/', views.razerKEY2, name='razerKEY2/'),
    path('razerKEY3/', views.razerKEY3, name='razerKEY3/'),
    path('razerKEY4/', views.razerKEY4, name='razerKEY4/'),
    path('razerKEY5/', views.razerKEY5, name='razerKEY5/'),

    # CORSAIR KEYBOARD
    path('corKEY1/', views.corKEY1, name='corKEY1/'),
    path('corKEY2/', views.corKEY2, name='corKEY2/'),
    path('corKEY3/', views.corKEY3, name='corKEY3/'),
    path('corKEY4/', views.corKEY4, name='corKEY4/'),
    path('corKEY5/', views.corKEY5, name='corKEY5/'),


]

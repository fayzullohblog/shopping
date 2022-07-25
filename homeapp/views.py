import re
from django.shortcuts import render
from shopapp.models import  AdvertisModel
from homeapp.models import ProductModel

def index(request):
    advertismodel= AdvertisModel.objects.all()[:1]
    context={'advertismodel':advertismodel}

    return render(request=request,template_name='index.html',context=context)

def index2(request):
    return render(request=request,template_name='index2.html')


def aboutview(request):
    return render(request=request,template_name='about.html')


def page404view(request):
    return render(request=request,template_name='pages/page404.html')


def faqview(request):
    return render(request=request,template_name='pages/faq.html')

def comingsoonview(request):
    return render(request=request,template_name='pages/comingsoon.html')

def cartpageview(request):
    return render(request=request,template_name='pages/cartpage.html')

def checkoutview(request):
    return render(request=request,template_name='pages/checkout.html')

def ordertrackingview(request):
    return render(request=request,template_name='pages/ordertracking.html')

def ordertrackingview(request):
    return render(request=request,template_name='pages/ordertracking.html')

def ordertrackingview(request):
    return render(request=request,template_name='pages/ordertracking.html')

def contactview(request):
    return render(request=request,template_name='pages/contact.html')

def empatycartview(request):
    return render(request=request,template_name='pages/empaty_cart.html')

def shop_list_leftview(request):
    return render(request=request,template_name='shopes/shop_list_left.html')

def singleproductview(request):
    return render(request=request,template_name='shopes/shop_list_left.html')

def productgaleryview(request):
    return render(request=request,template_name='shopes/productgalery.html')

def compareview(request):
    return render(request=request,template_name='shopes/compare.html')


def accounteview(request):
    return render(request=request,template_name='account.html')

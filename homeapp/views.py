from django.shortcuts import render
from shopapp.models import  AdvertisModel
from homeapp.models import ProductModel
from datetime import datetime
# delta=timedelta(
#    hours=8,
#    minutes=50,
#    seconds=50,
# )
def index(request):
    # <!-- Section Title & Tab End -->

    advertismodel= AdvertisModel.objects.get(id=1)
    productmodel=ProductModel.objects.all().order_by('?')[:8]
    productmodel_new_arrivals=ProductModel.objects.all().order_by('-create_date')[:8]
    productmodel_top_rated=ProductModel.objects.all()
    date_time=datetime(year=1,month=2,day=2,hour=4,minute=50,second=20,microsecond=34354)
    # productmodel_top_ratedning eng  kuringan va like bosilganlarni qilib pages junatiladi
    # <!-- Section Title & Tab End -->
    # <!-- Feature product area start -->

    #  narxi eng arzon maxsulatni filter qilish
    product_model_area=ProductModel.objects.last()
    productlastsecond=ProductModel.objects.get(id=product_model_area.id-1)
    product_area_minprice=ProductModel.objects.all()
    productprice=[]
    for i in range(1,product_area_minprice.count()+1):
      
        productprice.append(int((ProductModel.objects.get(id=i).price)))

    minprice=min(productprice)
    minproduct=ProductModel.objects.filter(price=minprice)

    #     foizi eng katta bulgan maxsulatni filter qilish

    productdiscount=[]
    for i in range(1,ProductModel.objects.all().count()+1):
        productdiscount.append(int((ProductModel.objects.get(id=i).discount)))
    maxdiscount=max(productdiscount)
    max_productmodel_discount=ProductModel.objects.filter(discount=maxdiscount)

    print('max_productmodel_discount',max_productmodel_discount)
   
    # <!-- Feature product area start -->
        
        

    context={
            'advertismodel':advertismodel,
            'productmodel':productmodel,
            'productmodel_new_arrivals':productmodel_new_arrivals,
            'productmodel_top_rated':productmodel_top_rated,
            'product_model_area':product_model_area,
            'productlastsecond':productlastsecond,
            'date_time':date_time,
            'minproduct':minproduct,
            'max_productmodel_discount':max_productmodel_discount

            }
    # for i in productmodel_top_rated:

    
        
   
   




    
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

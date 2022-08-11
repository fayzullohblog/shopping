from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from shopapp.models import  AdvertisModel, CartModel
from homeapp.models import CategoryModel, ColorModel, LikeModel, ProductModel
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

   
    # <!-- Feature product area start -->
    if request.method=='POST' and request.POST.get('cartid'):

        cartid=request.POST.get('cartid')
        
        title=ProductModel.objects.get(id=cartid)
        price=title.price
        image=title.image
        cart_count=title.product_count
        owner=request.user
       
        CartModel.objects.create(
            title=title,
            price=price,
            image=image,
            cart_count=cart_count,
            owner=owner,
            create_date=datetime.now()
        )
        return redirect('indexview')
    
    elif request.method=='POST' and request.user.is_authenticated:
        productid=request.POST.get('productid')
        product=ProductModel.objects.get(id=int(productid))
        
       
        try:
            likemodel=LikeModel.objects.get(owner=request.user,product=product)
            likemodel.delete()
        except:
            
            product=ProductModel.objects.get(id=request.POST.get('productid'))
            owner=request.user
            LikeModel.objects.create(
                owner=owner,
                product=product,
            )


    # product part cart 
    productcart=ProductModel.objects.all().order_by('-create_date')[:3]
    cartmodel=CartModel.objects.all().order_by('-create_date')[:3]
    # product end part cart

    context={
            'advertismodel':advertismodel,
            'productmodel':productmodel,
            'productmodel_new_arrivals':productmodel_new_arrivals,
            'productmodel_top_rated':productmodel_top_rated,
            'product_model_area':product_model_area,
            'productlastsecond':productlastsecond,
            'date_time':date_time,
            'minproduct':minproduct,
            'max_productmodel_discount':max_productmodel_discount,
            'cartmodel':cartmodel,
            'cartcount':CartModel.objects.all().count()
            }
    # for i in productmodel_top_rated:

    
    return render(request=request,template_name='index.html',context=context)
def deleteView(request, id):
    cart = CartModel.objects.get(id=id)
    cart.delete()
    return HttpResponseRedirect('/')

def cartview(request):
    cartmodel=CartModel.objects.all().order_by('-create_date')[:3]
    totalcart=''
    if request.method=='POST':
        totalcart=request.POST.get('totalcart')
        
    
        
    if request.method=="POST":
        cartmodel=CartModel.objects.all()
        cartmodel.delete()
        return HttpResponseRedirect('/cart/')
    context={
            'cartmodel':cartmodel,
            'totalcart':totalcart,
            }
    return render(request=request,template_name='shopes/cart.html',context=context)

def deletecart(request,id):
    cartmodel=CartModel.objects.get(id=id)
    cartmodel.delete()
    return HttpResponseRedirect('/cart/')
    
def shop_list_leftview(request):
    categories=CategoryModel.objects.all()
    categories_count=categories.count()
    products=ProductModel.objects.all()
    colormodel=ColorModel.objects.all()
    maxprice=''
    categoryid1=''
    
    

    
    if request.method=='GET':
        category_get=request.GET.get('category')
        price_get=request.GET.get('price')
        color_get=request.GET.get('color')
        brand_get=request.GET.get('brand')
        maxprice=request.GET.get('maxprice')
        categoryid1=request.GET.get('category_get')
        colorid=request.GET.get('colorid')
        colorcategoryid=request.GET.get('colorcategoryid')
        colormaxprice=request.GET.get('colormaxprice')
        print('colorcategoryid',colorcategoryid)
        print('colormaxprice',colormaxprice)
        print('colorid',colorid)

        if price_get:
            price_get
        else:
            price_get=''
        
        if color_get:
            color_get
        else:
            color_get=''
        
        if brand_get:
            brand_get
        else:
            color_get=''
        
        if categoryid1 or category_get or categoryid1 or price_get or color_get or brand_get:
    
            if category_get:
                print('kirdi1')

                products=ProductModel.objects.filter(category=CategoryModel.objects.get(id=category_get))
                if price_get and categoryid1:
                
                    products=ProductModel.objects.filter(category=CategoryModel.objects.get(id=categoryid1))
                    products=products.filter(price__lt=int(price_get))

                    # if colorcategoryid and colormaxprice:
                    #     products=ProductModel.objects.filter(color=colorid,price__lt=int(colormaxprice),category=colorcategoryid)
            else:
                i=0
                if categoryid1:
                    i=i+1
                    print('kirdi2',i)
                    print('----categoryid1',categoryid1)
                    products=ProductModel.objects.filter(category=CategoryModel.objects.get(id=categoryid1 ))
                    if maxprice and categoryid1:
                        category=CategoryModel.objects.get(id=categoryid1)
                
                        products=category.producmodels.filter(price__lt=int(maxprice))

                        if price_get and categoryid1:
                            
                            products=ProductModel.objects.filter(category=CategoryModel.objects.get(id=categoryid1))
                            products=products.filter(price__lt=int(price_get))
                elif colorcategoryid:
                    print('kirdi3')
                    products=ProductModel.objects.filter(category=CategoryModel.objects.get(id=colorcategoryid ))
                    if colormaxprice and colorcategoryid:
                        category=CategoryModel.objects.get(id=colorcategoryid)
                
                        products=category.producmodels.filter(price__lt=int(colormaxprice))

                        if colormaxprice and colorcategoryid:
                            
                            products=ProductModel.objects.filter(color=colorid,price__lt=int(colormaxprice),category=colorcategoryid)
    
    context={
         
        'categories':categories,
        'categories_count':categories_count,
        'maxprice':maxprice,
        'products':products,
        'category_get':category_get,
        'categoryid1':categoryid1,
        'colormodel':colormodel,
        'colorid':colorid,
        
        }
    
    return render(
                request=request,
                template_name='shopes/shop_list_left.html',
                context=context,
                )






def index2(request):
    return render(request=request,template_name='index2.html')

def wishlistview(request):
    return render(request=request,template_name='pages/wishlist.html')






def aboutview(request):
    return render(request=request,template_name='about.html')


def page404view(request):
    return render(request=request,template_name='pages/page404.html')


def faqview(request):
    return render(request=request,template_name='pages/faq.html')

def comingsoonview(request):
    return render(request=request,template_name='pages/comingsoon.html')

# def cartpageview(request):
#     return render(request=request,template_name='pages/cartpage.html')

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


def singleproductview(request):
    return render(request=request,template_name='shopes/shop_list_left.html')

def productgaleryview(request):
    return render(request=request,template_name='shopes/productgalery.html')

def compareview(request):
    return render(request=request,template_name='shopes/compare.html')


def accounteview(request):
    return render(request=request,template_name='account.html')




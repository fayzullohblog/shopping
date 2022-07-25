from django.urls import path
from .views import (accounteview, faqview, index, index2,aboutview, 
ordertrackingview, page404view,comingsoonview,cartpageview,checkoutview,contactview,
empatycartview,shop_list_leftview,singleproductview,productgaleryview,compareview,)

urlpatterns = [
    path('',index,name='indexview'),
    path('index2/',index2,name='index2view'),
    path('about/',aboutview,name='aboutview'),
    path('page404/',page404view,name='page404view'),
    path('ordertracking/',ordertrackingview ,name='ordertrackingview'),
    path('faq/',faqview ,name='faqview'),
    path('coming_soon/',comingsoonview,name='comingsoonview'),
    path('cartpageview/',cartpageview,name='cartpageview'),
    path('checkout/',checkoutview,name='checkoutview'),
    path('contact/',contactview,name='contactview'),
    path('empatycart/',empatycartview,name='empatycartview'),
    path('shop_list_left/',shop_list_leftview,name='shop_list_leftview'),
    path('singleproduct/',singleproductview,name='singleproductview'),
    path('productgalery/',productgaleryview,name='productgaleryview'),
    path('compare/',compareview,name='compareview'),
    path('account/',accounteview,name='accountview')

]
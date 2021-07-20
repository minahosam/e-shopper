from django.urls import path
from .views import *
app_name='main'
urlpatterns = [
    path('',show_all_product,name='show'),
    path('detail/<slug>/',product_detail,name='detail'),
    path('wish/<slug>/',wish_list,name='wish'),
    path('wishlist/',wishlist_page,name='wishlist'),
    path('search_c/',search_by_category,name='search_cat'),
    path('search_b/',search_by_brand,name='brand'),
    path('cart/',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('updateCart/',update_cart,name='cart_updation'),
    path('checkout/country/<str:country>',country_name_from_json,name='country_name')
]

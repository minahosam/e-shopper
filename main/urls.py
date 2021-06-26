from django.urls import path
from .views import *
app_name='main'
urlpatterns = [
    path('',show_all_product,name='show'),
    path('/<slug>',product_detail,name='detail')
]

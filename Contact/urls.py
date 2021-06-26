from django.urls import path
from .views import *
app_name='contact'
urlpatterns = [
    path('',show_contact_page,name='contact'),
    path('send/',sent_mail,name='send')
]

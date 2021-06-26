from django.shortcuts import render,redirect
from .models import *
from  .forms import *
from django.core.mail import send_mail
# Create your views here.
def show_contact_page(request):
    return render(request,'contact/contact.html',{})
def sent_mail(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    subject=request.POST.get('subject')
    message=request.POST.get('message')
    print(name+email+message+subject)
    send_mail(
            subject,
            f'sender name{name},sender mail{email},subject{subject},message{message}',
            email,
            ['eng_mina_hosam@yahoo.com'],
            fail_silently=False,
        )
    return redirect('contact:contact')
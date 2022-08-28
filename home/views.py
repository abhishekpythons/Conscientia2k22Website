from collections import UserList
from email.message import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.core.mail import EmailMessage

from django.contrib.auth import login
from django.utils.encoding import force_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site

from django.views.generic import View

from .tokens import token_generator

def index(request):
    return render(request,'index1.html')
    #return HttpResponse("Hello World. This is my app.")
# Create your views here.
def home(request):
   return render(request,'home.html')
def about(request):
   return render(request,'about.html')
def events(request):
    return render(request,'events.html')
def register(request):
    return render(request,'register.html')

def save(request):
    username = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    if not User.objects.filter(username=username).exists():
        if True: #not User.objects.filter(email=email).exists():
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.is_active = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))


            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64':uidb64, 'token':token_generator.make_token(user)})
            activate_url = 'https://' + domain + link
            email_subject = 'Activate your account'
            email_body = f'Hi there!, {user.username} use this link to verify your account \n{activate_url}'
            email_msg = EmailMessage(
                email_subject,
                email_body,
                'contact@conscientia.co.in',
                [email],
            )
            email_msg.send()
            print('sent successfully')
            return HttpResponse(f'email sent successfully to name:-{username}; email:-{email}; pass:-{password}')
    return HttpResponse(f'not sent name:-{username}; email:-{email}; pass:-{password}')

def authenticate_defined(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('home')


class VerificationView(View):
    def get(self, request, uidb64, token):
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.all().filter(pk=uid)[0]
        user.is_active = True
        user.save()
        return redirect('login')

def contact(request):
    return render(request,'contacts.html')
def login_defined(request):
    return render(request,'login.html')
    
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
    path('events', views.events, name='events'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_defined, name='login'),

    path('save', views.save, name='save'),
    path('authenticate', views.authenticate_defined, name='authenticate_defined'),
    path('activate/<uidb64>/<token>',views.VerificationView.as_view(), name='activate'),
]
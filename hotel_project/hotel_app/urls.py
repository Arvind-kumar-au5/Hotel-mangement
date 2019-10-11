from django.urls import path,include
from hotel_app import views

urlpatterns =[
path('',views.BaseView.as_view(),name='base'),
path('home/',views.IndexView.as_view(),name='index'),
path('register/',views.register,name='register'),
path('user_login/',views.user_login,name='user_login'),
path('advance_booking/',views.advance_booking,name='advance_booking'),
path('about/',views.about,name='about'),
path('thank/',views.thank,name = 'thank'),
path('room_terrif/',views.room_terrif,name='room_terrif'),
path('other/',views.other,name='other'),

]
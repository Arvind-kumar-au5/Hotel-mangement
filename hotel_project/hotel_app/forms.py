from django import forms
from django.contrib.auth.models import User
from hotel_app.models import UserProfileInfo,CustomerInfo
import random


class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model=User
		fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model=UserProfileInfo
		fields=('portfolio_Site','profile_pic')

class DateInput(forms.DateInput):
	input_type = 'date'        

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model= CustomerInfo
        fields= ["customer_id","customer_name","date","room_type","number_room","number_days"]	 
        
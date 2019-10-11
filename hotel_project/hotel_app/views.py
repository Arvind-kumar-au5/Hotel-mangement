from django.shortcuts import render
from django.views.generic import TemplateView
from hotel_app.forms import UserProfileInfoForm,UserForm,CustomerInfoForm
from hotel_app.models import CustomerInfo
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from . import forms


# Create your views here.

class IndexView(TemplateView):
    template_name = 'hotel_app/index.html'

class BaseView(TemplateView):
    template_name = 'hotel_app/base.html'

# function based view


def register(request):
    register=False

    if request.method == "POST":
        # user and profile data collect
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # validation
        if user_form.is_valid() and profile_form.is_valid():
            user =user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.propfile_pic = request.FILES['profile_pic']
            profile.save()

            register = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'hotel_app/registration.html',{'user_form' : user_form,'profile_form':profile_form , 'register': register})

def user_login(request):

    if request.method ==   'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password )
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('advance_booking'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed ")
            print("Username: {} and password {}".format(username,password))
    else:
        return render (request,'hotel_app/login.html',{})   
    

@login_required
def thank(request):
    return render(request,'hotel_app/thank.html')


@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')

@login_required
def advance_booking(request):
    form = CustomerInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.save())
        form = CustomerInfoForm()
        return HttpResponseRedirect(reverse('thank'))
    context = {
        'form': form
    }
    return render(request, "hotel_app/advance.html", context)

    
def about(request):
    return render(request,'hotel_app/about.html')

def room_terrif(request):
    return render(request, 'hotel_app/room_teriff.html')  

def other(request):
    return render(request,'hotel_app/other.html')      
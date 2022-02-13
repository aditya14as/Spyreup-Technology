from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .models import extendeduser
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_obj = User.objects.filter(username__iexact = username).first()
        if user_obj is None:
            messages.warning(request, 'User not found.')
            return redirect('login')
        
        
        profile_obj = extendeduser.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.warning(request, 'Profile is not verified check your mail.')
            return redirect('login')

        user = auth.authenticate(username = username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('webdevelopment')
        
        else:
            messages.warning(request, 'Wrong password.')
            return redirect('login')

    return render(request, 'webpages/accounts/login.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,'Email already exists')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(first_name=firstname,username=username, last_name=lastname, email=email, password=password)
                    phone =request.POST['phone']
                    auth_token = str(uuid.uuid4())
                    newextendeduser = extendeduser(phone=phone,user=user,auth_token = auth_token)
                    newextendeduser.save()
                    send_mail_after_registration(email , auth_token)
                    messages.warning(request, 'We have sent an email to you for verification, Please check your mail!')
                    return redirect('signup')

        else:
            messages.warning(request, 'Password do not match')
            return redirect('signup')

    return render(request, 'webpages/accounts/signup.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def verify(request , auth_token):
    try:
        profile_obj = extendeduser.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login')
        else:
            messages.warning(request, 'Error in verification')
            return redirect('login')

    except Exception as e:
        return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    orders=Order.objects.filter(user_id=request.user.id)
    return render(request, 'webpages/accounts/dashboard.html',{'orders':orders})

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi there, Click the link to verify your account http://127.0.0.1:8000/accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )



def ChangePassword(request , token):
        context = {}
    

        profile_obj = extendeduser.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            newpassword = request.POST.get('newpassword')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.warning(request, 'User not found.')
                return HttpResponseRedirect(request.path_info)
                
            
            if  newpassword != confirm_password:
                messages.warning(request, "Both password doesn't match.")
                return HttpResponseRedirect(request.path_info)
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(newpassword)
            user_obj.save()
            return redirect('login')
            
            
            
        
        
        return render(request , 'webpages/accounts/change-password.html' , context)




def ForgetPassword(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            
            if not User.objects.filter(email=email).first():
                messages.warning(request, 'No user found with this mail.')
                return redirect('forget-password')
            
            user_obj = User.objects.get(email = email)
            token = str(uuid.uuid4())
            profile_obj= extendeduser.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.warning(request, 'An email is sent for reset password')
            return redirect('forget-password')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'webpages/accounts/forget-password.html')



def send_forget_password_mail(email , token ):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/accounts/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
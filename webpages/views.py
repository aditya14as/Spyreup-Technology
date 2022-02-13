
from django.shortcuts import render, redirect
from .models import Slider, Plan
from blog.models import Blog
from django.contrib.auth.decorators import login_required
API_KEY = '{API_KEY}'
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    blogs = Blog.objects.filter().order_by('-pub_date')[:3]

    

    data = {
        'sliders': sliders,
        'blogs': blogs,
    }
    return render(request, 'webpages/home.html',data)

def webdevelopment(request):
    basic = Plan.objects.all().filter(plan_types__iexact = 'Basic')
    standard = Plan.objects.all().filter(plan_types__iexact = 'Standard')
    premium = Plan.objects.all().filter(plan_types__iexact = 'Premium')
    
    data = {
        'basic': basic,
        'standard': standard,
        'premium': premium,
    }

    return render(request, 'webpages/webdevelopment.html', data)

# def appdevelopment(request):
#     return render(request, 'webpages/appdevelopment.html')

def technews(request):
    return render(request, 'webpages/news/homenews.html')

def contact(request):
    return render(request, 'webpages/contact.html')


# @login_required(login_url='login')
# def checkout(request):
#     plan = request.POST.get('plan')
#     price = request.POST.get('price')

#     return render(request, 'webpages/order/checkout.html',{'plan':plan, 'price':price})

# @login_required(login_url='login')
# def order(request):
#     if request.method == 'POST':
#         name = request.POST.get('first_name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         amount = int(request.POST.get('amount')) * 100
#         plan = request.POST.get('plan')
#         client = razorpay.Client(auth=("rzp_test_QvAdAXlcxbsrF0", "re1VL4UDLrb5P6rzVEiWiKfp"))
#         payment = client.order.create({'amount':amount, 'currency':'INR','payment_capture': '1'})
#         user_id = request.POST.get('user_id')
#         order = Order(name=name, phone=phone, email=email, payment_id =payment['id'], amount=amount/100, plan=plan, user_id=user_id)
#         order.save()
#         return render(request, "webpages/order/order.html", {'payment': payment})

#     return render(request, 'webpages/order/order.html')

# @csrf_exempt
# @login_required(login_url='login')
# def success(request):
#     if request.method == "POST":
#         a = request.POST
#         order_id = ""
#         for key, val in a.items():
#             if key == "razorpay_order_id":
#                 order_id =val
#                 break
#         user = Order.objects.filter(payment_id = order_id).first()
#         user.paid = True
#         user.save()
#     return render(request, 'webpages/order/success.html')




from django.shortcuts import render, redirect
from django.http import Http404
from .models import Order
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.


@login_required(login_url='login')
def checkout(request):
    plan = request.POST.get('plan')
    price = request.POST.get('price')
    if not get_referer(request):
        return redirect('webdevelopment')

    return render(request, 'webpages/order/checkout.html',{'plan':plan, 'price':price})

@login_required(login_url='login')
def order(request):
    if not get_referer(request):
        raise Http404
    if request.method == 'POST':
        name = request.POST.get('first_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        amount = int(request.POST.get('amount')) * 100
        plan = request.POST.get('plan')
client = razorpay.Client(auth=("{}RAZOR_PAY_KEY}", "{RAZOR_PAY_PRIVATE_KEY}"))
        payment = client.order.create({'amount':amount, 'currency':'INR','payment_capture': '1'})
        user_id = request.POST.get('user_id')
        order = Order(name=name, phone=phone, email=email, payment_id =payment['id'], amount=amount/100, plan=plan, user_id=user_id)
        order.save()
        return render(request, "webpages/order/order.html", {'payment': payment})

    return render(request, 'webpages/order/order.html')

@csrf_exempt
def success(request):
    if not get_referer(request):
        raise Http404

    if request.method == "POST":
        a = request.POST
        order_id = ""
        data = {}
        for key, val in a.items():
            if key == "razorpay_order_id":
                data['razorpay_order_id']=val
                order_id=val
            elif key == 'razorpay_payment_id':
                data['razorpay_payment_id'] =val
            elif key == 'razorpay_signature':
                data['razorpay_signature']=val
        user = Order.objects.filter(payment_id = order_id).first()


        client = razorpay.Client(auth=("{RAZOR_PAY_KEY}", "{RAZOR_PAY_PRIVATE_KEY}"))
        check = client.utility.verify_payment_signature(data)
        if check:
            return render(request,'webpages/order/error.html')

        user.paid = True
        user.save()
    return render(request, 'webpages/order/success.html')


def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer
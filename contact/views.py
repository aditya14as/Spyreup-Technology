from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages
# Create your views here.
def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']

        contact = Contact(first_name=first_name, phone=phone, email=email, company=company, subject=subject, message=message, user_id=user_id)
        contact.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('contact')

    return render(request, 'webpages/contact.html')

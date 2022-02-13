from django.urls import path
from . import views
 

urlpatterns = [
    path('checkout/',views.checkout, name="checkout"),
    path('order/',views.order, name="order"),
    path('success/',views.success, name="success"), 
]
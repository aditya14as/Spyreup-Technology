from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login',views.login, name="login"),
    path('signup',views.signup, name="signup"),
    path('logout',views.logout_user, name="logout"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('verify/<auth_token>' , verify , name="verify"),
    path('forget-password/' , ForgetPassword , name="forget-password"),
    path('change-password/<token>/' , ChangePassword , name="change-password"),
    
]
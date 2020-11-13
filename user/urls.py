from django.urls import path
from . import views


urlpatterns = [
    path('login.html', views.loginView, name='login'),
    path('register.html', views.registerView, name='register'),
    path('setpassword.html', views.setpasswordView, name='setpassword'),
    path('logout.html', views.logoutView, name='logout'),
    path('findPassword.html', views.findPassword, name='findPassword'),
    path('user_center_info.html', views.user_center_infoView, name='user_center_info'),
    path('user_center_order.html', views.user_center_orderView, name='user_center_order'),
    path('user_center_site.html', views.user_center_siteView, name='user_center_site'),
]

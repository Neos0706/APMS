from django.urls import path
from . import views


urlpatterns = [

    path('cart.html', views.cart, name='cart'),

]
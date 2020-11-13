from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.ap, name='ap'),
    # 第一个d+为类型的id, 第二个为当前是第几页,第三个是排序的依据
    # path('list(\d+)_(\d+)_(\d+)', views.list, name='list'),
    re_path('list(?P<tid>[0-9]{1})_(?P<pindex>[0-9]{1})_(?P<sort>[0-9]{1})', views.list, name='list'),
    # path(r'^list(\d+)_(\d+)_(\d+)/$', views.list, name='list'),
    path('detail.html', views.detail, name='detail'),
    path('cart.html', views.cart, name='cart'),
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from user.models import MyUser
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def ap(request):
    username = request.user.username
    # 查询各分类的最新4条,最热4条信息
    typelist = TypeInfo.objects.all()  # 首先获得外键指向的表中对象，然后通过‘_set’这样的方法获得目标表中的数据
    type0 = typelist[0].product_set.order_by('-id')[0:4]  # 按降序获得,获得最大的
    type01 = typelist[0].product_set.order_by('-ap_click')[0:4]
    type1 = typelist[1].product_set.order_by('-id')[0:4]
    type11 = typelist[1].product_set.order_by('-ap_click')[0:4]
    type2 = typelist[2].product_set.order_by('-id')[0:4]
    type21 = typelist[2].product_set.order_by('-ap_click')[0:4]
    type3 = typelist[3].product_set.order_by('-id')[0:4]
    type31 = typelist[3].product_set.order_by('-ap_click')[0:4]
    type4 = typelist[4].product_set.order_by('-id')[0:4]
    type41 = typelist[4].product_set.order_by('-ap_click')[0:4]
    type5 = typelist[5].product_set.order_by('-id')[0:4]
    type51 = typelist[5].product_set.order_by('-ap_click')[0:4]
    context = {
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }
    return render(request, 'ap.html', context, locals())


def list(request, tid, pindex, sort):  # 列表页     #分别为类型的id,第几页,按什么排序
    typeinfo = TypeInfo.objects.get(id=int(tid))
    news = typeinfo.product_set.order_by('-id')[0:2]  # 取该类型最新的两个
    if sort == '1':   # 默认  最新
        goods_list = Product.objects.filter(ap_type_id=int(tid)).order_by('-id')
        # print(22233)
    elif sort == '2':     # 按价格排序
        goods_list = Product.objects.filter(ap_type_id=int(tid)).order_by('-ap_price')
    elif sort == '3':
        goods_list = Product.objects.filter(ap_type_id=int(tid)).order_by('-ap_click')
    paginator = Paginator(goods_list, 10)         # 分页, 每页有几个元素
    page = paginator.page(int(pindex))          # 获得pindex页的元素列表
    context = {
        'page': page,        # 排序后的每页的元素列表
        'typeinfo': typeinfo,    # 类型信息
        'news': news,    # 新品推荐列表
        'sort': sort,    # 传递排序数字, 方便图标active
        'paginator': paginator,  # 分页
    }
    return render(request, 'list.html', context)


def detail(request, id):        # 详情页    # 商品id
    goods = Product.objects.get(id=int(id))
    goods.gclick = goods.gclick + 1     #点击量
    goods.save()
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'goods': goods,
        'news': news,
        'id': id,
    }
    response = render(request, 'detail.html', context)
    # 记录最近浏览,在用户中心使用
    if request.session.has_key('user_id'):  # 判断是否已经登录
        key = str(request.session.get('user_id'))
        goods_ids = request.session.get(key, '')
        # print(type(goods_ids))
        # print(goods_ids)
        goods_id = str(goods.id)  # 将int型转化为str类型
        if goods_ids != '':  # 判断是否有浏览记录,如果则继续判断
            # goods_ids = goods_ids.split(',')  # 以逗号分隔切片    切片后为list型
            if goods_ids.count(goods_id) >= 1:  # 如果已经存在,删除掉
                goods_ids.remove(goods_id)
            goods_ids.insert(0, goods_id)  # 添加到第一个
            if len(goods_ids) >= 6:  # 如果超过6个则删除最后一个
                del goods_ids[5]
        else:
            goods_ids = []
            goods_ids.append(goods_id)
        # print(type(goods_ids))
        # print(goods_ids)
        request.session[key] = goods_ids
    return response


@login_required(login_url='/user/login.html')
def cart(request):
    return render(request, 'cart.html', locals())




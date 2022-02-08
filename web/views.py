from django.shortcuts import render, HttpResponse, redirect
from web.models import friends_info
# Create your views here.


def home(request):
    return HttpResponse("Home page")


def users_list(request):
    return render(request, "users_list.html")


def users_add(request):
    return render(request, "users_add.html")


def reused_model(request):

    name = "hxx"

    hobby = ["画画", "调酒", "排球"]

    hxx_info = {'name': 'hxx', 'hobby': hobby}

    info_list = [
        {'name': 'hxx', 'hobby': hobby},
        {'name': 'zwx', 'hobby': ["尝试新事物", "享乐", "变得更好"]},
        {'name': 'xjl', 'hobby': ["看剧", "听音乐", "打游戏"]},
        {'name': 'whh', 'hobby': ["篮球", "排球", "打游戏"]},
    ]

    return render(request, "reused_model.html", {"n1": name, "h1": hobby, 'f1': hxx_info, 'l1': info_list})


def friends(request):
    return render("friends.html")


def data_process():
    # #### 1.新建 ####
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="运营部")
    # UserInfo.objects.create(name="武沛齐", password="123", age=19)
    # UserInfo.objects.create(name="朱虎飞", password="666", age=29)
    # UserInfo.objects.create(name="吴阳军", password="666")

    # #### 2.删除 ####
    # UserInfo.objects.filter(id=3).delete()
    # Department.objects.all().delete()

    # #### 3.获取数据 ####
    # 3.1 获取符合条件的所有数据
    # data_list = [对象,对象,对象]  QuerySet类型
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)

    # data_list = [对象,]
    # data_list = UserInfo.objects.filter(id=1)
    # print(data_list)
    # 3.1 获取第一条数据【对象】
    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)


    # #### 4.更新数据 ####
    # UserInfo.objects.all().update(password=999)
    # UserInfo.objects.filter(id=2).update(age=999)
    # UserInfo.objects.filter(name="朱虎飞").update(age=999)
    return


def friends_info_list(req):
    data_list = friends_info.objects.all()

    return render(req, "friends_info.html", {"data_list": data_list})


def friends_add(req):
    if req.method == "GET":
        return render(req, "friends_add.html")

    # 获取用户提交的数据
    name = req.POST.get("name")
    birthday = req.POST.get("birthday")
    hobby = req.POST.get("hobby")

    # 添加到数据库
    friends_info.objects.create(name=name, birthday=birthday, hobby=hobby)
    return redirect("/friends/info")


def friends_delete(req):
    # 删除朋友
    nid = req.GET.get('nid')
    friends_info.objects.filter(id=nid).delete()
    return redirect("/friends/info")


def friends_edit(req):
    # 修改信息
    return render(req, "friends_edit.html")
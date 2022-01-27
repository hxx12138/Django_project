from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Home page")


def users_list(request):
    return render(request, "users_list.html")


def users_add(request):
    return render(request, "users_add.html")
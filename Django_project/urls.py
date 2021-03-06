from web import views
"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', views.home),
    path('users_list/', views.users_list),
    path('users_add/', views.users_add),
    path('reused_model/', views.reused_model),
    path('friends/', views.friends),

    # 好朋友信息管理系统
    path('friends/info', views.friends_info_list),
    path('friends/add', views.friends_add),
    path('friends/delete', views.friends_delete),
    path('friends/edit', views.friends_edit),
    path('friends/echart', views.friends_echart),
    path('friends/hobby', views.friends_hobby),
    path('friends/project_3D', views.project_3D),
]

"""
URL configuration for project36 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SchoolProject/',SchoolProject.as_view(),name='SchoolProject'),
    path('Schoolcreate/',Schoolcreate.as_view(),name='Schoolcreate'),



    re_path('^update/(?P<pk>\d+)/',SchoolUpdate.as_view(),name='update'),
    re_path('(?P<pk>\d+)/',SchoolDetail.as_view(),name='SchoolDetails'),
]

"""
URL configuration for djangomodels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from myapp.views import home, student_create, student_update,student_get,student_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('student-create/',student_create,name='student_create'),
    path('student-update/',student_update,name='student_update'),
    path('student-delete/<int:id>',student_delete,name='student_delete'),
    path('student-get/<int:id>',student_get,name='student_get')
                
]

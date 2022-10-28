"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from api.views import AccesibleElementView, AccesibleElementViewID, DishTypeView, DishTypeViewID, DishView, DishViewID, ClassroomView, ClassroomViewID, TaskView, TaskViewID

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accesible_element', AccesibleElementView),
    path('api/accesible_element/<_id>', AccesibleElementViewID),
    path('api/dish_type', DishTypeView),
    path('api/dish_type/<_id>', DishTypeViewID),
    path('api/dish', DishView),
    path('api/dish/<_id>', DishViewID),
    path('api/classroom', ClassroomView),
    path('api/classroom/<_id>', ClassroomViewID),
    path('api/task', TaskView),
    path('api/task/<_id>', TaskViewID),
]

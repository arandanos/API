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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accessible_element', AccessibleElementView),
    path('api/accessible_element/<_id>', AccessibleElementViewID),
    path('api/dish_type', DishTypeView),
    path('api/dish_type/<_id>', DishTypeViewID),
    path('api/dish', DishView),
    path('api/dish/<_id>', DishViewID),
    path('api/classroom', ClassroomView),
    path('api/classroom/<_id>', ClassroomViewID),
    path('api/feedback', FeedbackView),
    path('api/task', TaskView),
    path('api/task/<_id>', TaskViewID),
    path('api/kitchen_order', KitchenOrderView),
    path('api/kitchen_order/<_id>', KitchenOrderViewID),
    path('api/kitchen_order/task/<_id>', KitchenOrderViewTaskID),
    path('api/kitchen_order_detail', KitchenOrderDetailView),
    path('api/kitchen_order_detail/<_id>', KitchenOrderDetailViewID),
    path('api/kitchen_order_detail/<_classroom>/<_kitchen_order>', KitchenOrderDetailViewClassOrder),
    path('api/material_type', MaterialTypeView),
    path('api/material', MaterialView),
    path('api/material/<_id>', MaterialViewID),
    path('api/material_task', MaterialTaskView),
    path('api/material_task/<_id>', MaterialTaskViewID),
    path('api/material_task/task/<_id>', MaterialTaskViewTaskID),
    path('api/material_task_detail', MaterialTaskDetailView),
    path('api/material_task_detail/<_id>', MaterialTaskDetailViewID),
    path('api/image/<_image>', ImageViewID)
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

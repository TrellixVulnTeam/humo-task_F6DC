from django.contrib import admin
from django.urls import path
from restAPI.views import categories_list, category_detail, services_list, service_detail, status_list, status_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/all/', categories_list),
    path('category/detail/<pk>', category_detail),
    path('service/all/', services_list),
    path('service/detail/<pk>', service_detail),
    path('status/all/', status_list),
    path('status/detail/<pk>', status_detail),
]
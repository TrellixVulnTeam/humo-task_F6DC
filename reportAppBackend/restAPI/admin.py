from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Status, Category, Service
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Status)
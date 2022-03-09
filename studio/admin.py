from django.contrib import admin
from .models import Trainer, Category, Equipment, Classes, Client

# Register your models here.

class ClassesAdmin(admin.ModelAdmin):
    list_filter = ("trainer","title")
    list_display = ("title",)
    prepopulated_fields = {"slug":("title",)}

class ClientAdmin(admin.ModelAdmin):
    list_filter = ("last_name","email")
    list_display = ("first_name","last_name","email","phone")
    
admin.site.register(Trainer)
admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Client)
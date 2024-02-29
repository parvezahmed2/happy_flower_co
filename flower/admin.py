from django.contrib import admin
from .models import Flower, Order, Category
# Register your models here.



class ModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    lsit_display = ['name', 'slug']

admin.site.register(Category, ModelAdmin)
admin.site.register(Flower)
admin.site.register(Order)
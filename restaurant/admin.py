from django.contrib import admin
from restaurant.models import Category, Dish, Picture

# Register your models here.
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Picture)
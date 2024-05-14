from django.contrib import admin
from .models import User, People, Product, Category

admin.site.register(User)
admin.site.register(People)
admin.site.register(Product)
admin.site.register(Category)
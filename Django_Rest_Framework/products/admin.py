from django.contrib import admin
from django.contrib.auth.models import User
from .models import ProductComment
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ProductComment)
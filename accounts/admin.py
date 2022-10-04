from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CoUserAdmin(admin.ModelAdmin):
   pass


admin.site.register(CustomUser, CoUserAdmin)

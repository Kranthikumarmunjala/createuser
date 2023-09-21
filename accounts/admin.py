from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display=['id','name','phone_number']




admin.site.register(CustomUser)


UserAdmin.fieldsets+=(
    (
        'customfields',{
            'fields':('phone_number','address')
        }
    )
)
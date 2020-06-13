from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from .forms import xUserCreationForm
from .models import Xusers

# class UserAdmin(BaseUserAdmin):
    
    
#     add_form = xUserCreationForm
    
#     list_display = ('email','admin')
#     list_filter = ('email',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ()}),
#         ('Permissions', {'fields': ('admin',)}),
#     )
    
#     add_fieldsets = (
#         (None,{
#             'classes': ('wide',),
#             'fields':('email','password','password2')
#         }),
#     )
    
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()

# class xUserAdmin(UserAdmin):
    
admin.site.register(Xusers)

# admin.site.register()
# admin.site.unregister(Group)

# Register your models here.

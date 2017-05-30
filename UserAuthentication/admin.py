from django.contrib import admin
from UserAuthentication import models

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('email','is_admin','memo')
    list_per_page = 10

admin.site.register(models.UserProfile,UserInfoAdmin)
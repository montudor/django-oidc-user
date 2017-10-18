from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
	list_display = ('name', 'username', 'is_staff', )
	list_filter = ('is_staff', )
	search_fields = ('first_name', 'last_name', 'username', )
	readonly_fields = ('date_joined', 'last_login', )
	fieldsets = (
		(None, {
			'fields': ('username', 'password')
		}),
		("Personal Information", {
			'fields': ('first_name', 'last_name', 'email')
		}),
		("Permissions", {
			'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
		}),
		("Important Dates", {
			'fields': ('last_login', 'date_joined')
		}),
	)
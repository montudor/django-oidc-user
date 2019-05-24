from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
	list_display = ('name', 'username', 'is_staff', )
	list_filter = ('is_staff', )
	search_fields = ('first_name', 'last_name', 'username', )
	readonly_fields = ('date_joined', 'last_login', 'updated_at', )
	fieldsets = (
		(None, {
			'fields': ('username', 'password')
		}),
		("Profile", {
			'fields': ('first_name', 'last_name', 'website')
		}),
		("Email", {
			'fields': ('email', 'email_verified')
		}),
		("Phone", {
			'fields': ('phone', 'phone_verified')
		}),
		("Permissions", {
			'fields': ('is_active', 'is_verified', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
		}),
		("Location", {
			'fields': ('zoneinfo', 'locale')
		}),
		("Important Dates", {
			'fields': ('last_login', 'date_joined', 'updated_at')
		}),
	)

# gangaGen/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Protein

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'access_code', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'access_code')
    fieldsets = (
        # ... other fields ...
        ('Custom Fields', {'fields': ('access_code',)}),
    )

class ProteinAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Protein._meta.fields]  # Display all fields

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Protein, ProteinAdmin)
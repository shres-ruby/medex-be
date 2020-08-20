from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Patient, Doctor, Prescription, HealthProfile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None,{'fields': ('email','password')}),
        ('Personal info', {'fields':('first_name','last_name','is_patient','is_doctor')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser')}),
    )
    
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields' : ('email','password1','password2','is_patient','is_doctor'),
        }),
    )
    list_display = ('email','first_name','last_name','is_staff','is_patient','is_doctor')
    search_fields = ('email','first_name','last_name')
    ordering = ('email',)


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Prescription)
admin.site.register(HealthProfile)
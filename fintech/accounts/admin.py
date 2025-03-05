from django.contrib import admin
from .models import User, PersonalAccount, BusinessAccount, OTPCODE

# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['username','email','is_staff','is_superuser','email_verified','phone_verified','account_type'] 


@admin.register(PersonalAccount)
class PersonalAccountAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','image',] 


@admin.register(BusinessAccount)
class BusinessAccountAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','company_name','registration_number','business_address','legal_name','logo'] 


@admin.register(OTPCODE)
class OTPcodeadmin(admin.ModelAdmin):
    list_display = ['user','email_otp','phone_otp','created_at',] 
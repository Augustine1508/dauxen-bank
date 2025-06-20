from django.contrib import admin
from .models import User, PersonalAccount, BusinessAccount, OTPCODE, TwofactorModel

# Register your models here.

@admin.register(TwofactorModel)
class TwofactorAdmin(admin.ModelAdmin):
    list_display = ['user','is_twofa_enabled','twofacode','twofactor_created','twofa_backup','is_email_enabled','email_otp','email_created','updated_at'] 


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['username','email','is_staff','is_superuser','email_verified','phone_verified','account_type',] 


@admin.register(PersonalAccount)
class PersonalAccountAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','image',]
    fields = ['user', 'date_of_birth', 'image'] 

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px; border-radius: 5px;" />', obj.image.url)
        return "No image"
    image_tag.short_description = 'Photo'


@admin.register(BusinessAccount)
class BusinessAccountAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','company_name','registration_number','business_address','legal_name','logo'] 


@admin.register(OTPCODE)
class OTPcodeadmin(admin.ModelAdmin):
    list_display = ['user','email_otp','phone_otp','created_at',] 
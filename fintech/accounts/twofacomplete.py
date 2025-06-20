from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from .models import TwofactorModel
import pyotp
from django.contrib.auth.mixins import LoginRequiredMixin




class SetupComplete(LoginRequiredMixin,View):
    login_url ='login'
    def post(self,request):
        login_user = request.user
        user_2fa  = TwofactorModel.objects.get_or_create(user=login_user)[0]
        twofacodes = user_2fa.twofacode

        if not twofacodes:
            return JsonResponse({"error": "TOTP secret not found."}, status=400)
        

        otp_token =  request.POST.get('otp_token')
        totp_code = pyotp.TOTP(twofacodes)
        if totp_code.verify(otp_token):
            user_2fa.is_twofa_enabled = True
            user_2fa.save()
            return JsonResponse({"success": "2FA setup complete."}, status=200)
        else:
             return JsonResponse({"error": "Invalid OTP token."}, status=400)



        
        




        



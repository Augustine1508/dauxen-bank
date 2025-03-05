from .models import OTPCODE
from django.views.generic import View
from django.http import JsonResponse
from .models import User, OTPCODE
from .emailotpsender import send_otp
from django.shortcuts import render

class Email_VerificationView(View):
    def get(self, request):
        return render(request, 'otpverify.html')

    
    def post(self, request):
        otp_user = request.POST["otp_code"]

        if not otp_user:
            return JsonResponse({'error': "verification code is not provided"}, status=400)
        
        try:
            user_otp_records = OTPCODE.objects.get(email_otp=otp_user)
            user = user_otp_records.user

        except OTPCODE.DoesNotExist:
            return JsonResponse({'error': "Invalid OTP"}, status=400)

        if user_otp_records.is_otp_expired():
            send_otp(user.email)
            return JsonResponse({'error': "Otp Expired, New Otp has been sent"}, status=400)

        if user.email_verified:
            return JsonResponse({'error': "Email Already Verified"}, status=400)
        user.email_verified = True
        user.save()
        return JsonResponse({'success': "Email Verified"}, status=200)





















# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views import View
# from .models import OTPCODE

# class Email_VerificationView(View):
#     def get(self, request):
#         return render(request, 'otpverify.html')

#     def post(self, request):
#         otp_user = request.POST.get("otp_code", None)

#         if not otp_user:
#             return JsonResponse({'error': "verification code is not provided"}, status=400)

#         try:
#             user_otp_records = OTPCODE.objects.get(email_otp=otp_user)
#             user = user_otp_records.user

#         except OTPCODE.DoesNotExist:
#             return JsonResponse({'error': "Invalid OTP"}, status=400)
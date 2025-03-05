from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from .emailotpsender import send_otp

from django.contrib.auth import get_user_model


User = get_user_model()


# Here is my view for registration or Signup
class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')


    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        account_type = request.POST['account_type']

        if not username or not email or not password2 or not password or not phone:
            return JsonResponse({'error': 'please fill all the form field'}, status=400)
            
        if password2 != password:
            return JsonResponse({'error': 'Passwords does not match'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)

        if User.objects.filter(phone=phone).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)

        user = User.objects.create(
            username=username,
            email=email,
            phone=phone,
            account_type=account_type,
            password=make_password(password)
        )
        send_otp(email)
        return JsonResponse({'success': 'Acccount Created Successfully'}, status=201)




from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

# Create your views here.


User = get_user_model()

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            return JsonResponse({'error': 'Please fill all the form fields'}, status=400)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Account not found'}, status=400)
        
        user = authenticate(request, email=email, password=password)
        if user is None:
            return JsonResponse({'error': 'Incorrect password'}, status=400)
        
        login(request, user)
        return JsonResponse({'success': 'Login successful'}, status=200)
























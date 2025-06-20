from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django_otp.decorators import otp_required

# @otp_required
class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')
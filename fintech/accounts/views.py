from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

class HomepageView(View):
    def get(self, request):
        return render(request, 'index.html')









class Login(View):
    def get(self, request):
        return render(request, 'login.html')
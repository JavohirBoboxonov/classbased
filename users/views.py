from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser

class RegisterPage(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if CustomUser.objects.filter(username = username).exists():
            return render(request, 'auth/register.html', {
                "error": "Bu username band"
            })

        if password != confirm_password:
            return render(request, 'auth/register.html', {
                "error":"Parollar Mos Emas"
            })
    
        user = CustomUser.objects.create(
            username = username,
            email = email,

        )
        user.set_password(password)
        user.save()
        return redirect('login')

class LoginPage(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,  username = username, password = password)
        if user is None:
            return render(request, 'auth/login.html',{
                "error":"Username yoki Parol Xato"
            })
        login(request, user)
        return redirect('home')

def Exit(request):
    user = request.user
    logout(request)
    return redirect('login')
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser, EmailCode
from .utils import generate_password


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
    
        user = CustomUser.objects.create_user(
            username = username,
            email = email,
            password = password,
            is_active = False
        )
        
        code = generate_password()

        send_mail(
            "Tasdiqlash Kodi",
            f"Sizning Tasdiqlash Kodingiz {code}",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently = False,
        )
        otp =  EmailCode.objects.create(user = user, code = code)
        otp.save()
        request.session['user_id'] = user.id
        return redirect('verify_email')

class VerifyPage(View):
    def get(self, request):
        return render(request, 'auth/verify.html')
    
    def post(self, request):
        code = request.POST.get('code')
        user_id = request.session.get('user')
        
        if not user_id:
            return redirect('login')
        
        email_code = EmailCode.objects.filter(
            user_id=user_id, 
            code=code, 
            is_active=False
        ).last()
        
        print(11111, email_code)
        
        if email_code:
            email_code.is_active = True
            email_code.save()

            request.session.flush()
            
            return redirect('login')
        else:
            return render(request, 'auth/verify.html', {
                'error': 'Kod noto\'g\'ri yoki eskirgan'
            })

class LoginPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'auth/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            return render(request, 'auth/login.html', {
                "error": "Barcha maydonlarni to'ldiring"
            })
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return render(request, 'auth/login.html', {
                "error": "Username yoki Parol Xato"
            })
        
        if not user.is_active:
            return render(request, 'auth/login.html', {
                "error": "Hisobingiz faol emas"
            })
        
        login(request, user)
        
        next_url = request.GET.get('next') or request.POST.get('next')
        if next_url:
            return redirect(next_url)
        
        return redirect('home')

def Exit(request):
    user = request.user
    logout(request)
    return redirect('login')
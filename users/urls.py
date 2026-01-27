from django.urls import path
from .views import RegisterPage, LoginPage, Exit


urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', Exit, name='logout')
]
from django.urls import path 
from .views import HomePage, DetailPage, CreatePage, UpdatePage, Delete

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('detail/<int:pk>/', DetailPage.as_view(), name='detail'),
    path('create/', CreatePage.as_view(), name='create'),
    path('update/<int:pk>/', UpdatePage.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete')
]
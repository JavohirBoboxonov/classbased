from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
# Create your views here.

class HomePage(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'index.html', {'product': product})

class DetailPage(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk = pk)
        return render(request, 'detail.html', {'product': product})

class CreatePage(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'create_product.html', {'product': product})
    
    def post(self, request):
        image = request.POST.get('image')
        title = request.POST.get('title')
        make_company = request.POST.get('make_company')
        composition = request.POST.get('composition')
        make_year = request.POST.get('make_year')
        limit_year = request.POST.get('limit_year')
        desc = request.POST.get('desc')

        product = Product.objects.create(
            image = image,
            title = title,
            make_company = make_company,
            composition = composition,
            make_year = make_year,
            limit_year = limit_year,
            desc = desc
        )
        product.save()
        return redirect('home')

from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

class UpdatePage(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk =pk)
        return render(request, 'update_page.html', {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk =pk)

        product.image = request.POST.get('image')
        product.title = request.POST.get('title')
        product.make_company = request.POST.get('make_company')
        product.composition = request.POST.get('composition')
        product.make_year = request.POST.get('make_year')
        product.limit_year = request.POST.get('limit_year')
        product.desc = request.POST.get('desc')

        product.save()

        return redirect('home')

class Delete(View):
    def get(self, request, pk):
        product = Product.objects.get(pk = pk)
        product.delete()
        return redirect('home')
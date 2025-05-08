from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products,
               'categories': categories}
    return render(request, 'shop/home.html', context)



def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product,
               'categories': Category.objects.all()}
    return render(request, 'shop/detail.html', context)

def category_detail(request, category_title):
    category = Category.objects.get(title=category_title)
    products = Product.objects.filter(category=category.id)
    context = {'products': products,
               'categories': Category.objects.all()}
    return render(request, 'shop/home.html', context)
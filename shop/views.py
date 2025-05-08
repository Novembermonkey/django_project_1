from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def home(request, category_title=None):
    if category_title:
        category_id = Category.objects.get(title=category_title).id
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()

    context = {'products': products,
               'categories': Category.objects.all()}
    return render(request, 'shop/home.html', context)



def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'products': product,
               'categories': Category.objects.all()}
    return render(request, 'shop/detail.html', context)


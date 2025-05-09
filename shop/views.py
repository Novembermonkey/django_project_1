from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from .forms import OrderForm
from .models import Product, Category, Order


# Create your views here.

def home(request, category_title=None):

    search = request.GET.get('search')
    if category_title:
        category_id = Category.objects.get(title=category_title).id
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()

    if search:
        products = products.filter(name__icontains=search)

    context = {'products': products,
               'categories': Category.objects.all()}

    return render(request, 'shop/home.html', context)



def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        context = {'product': product,
                   'categories': Category.objects.all()}
        return render(request, 'shop/detail.html', context)

    except Product.DoesNotExist:
        return HttpResponse('Product Not Found')

def order_detail(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('home')
        else:
            return form.errors.as_json()

    context = {'product': product,
               'form': form,
               }
    return render(request, 'shop/detail.html', context)

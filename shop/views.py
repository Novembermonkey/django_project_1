from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.contrib import messages
from django.db.models import Avg
from .forms import OrderForm, ProductForm, CommentForm
from .models import Product, Category, Comment
from django.contrib.auth.decorators import login_required
from decimal import Decimal


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
    products = products.annotate(rating = Avg('comments__rating')).order_by('-rating')
    context = {'products': products,
               'categories': Category.objects.all(),
               }

    return render(request, 'shop/home.html', context)



def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        context = {'product': product,
                   'categories': Category.objects.all(),
                   'comments': product.comments.all().order_by('-id')}
        return render(request, 'shop/detail.html', context)

    except Product.DoesNotExist:
        return HttpResponse('Product Not Found')

def order_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product

            if product.amount < order.quantity:
                messages.add_message( request,
                                      messages.ERROR,
                                      "Don't have enough products, please enter lesser amount")
            elif order.quantity == 0:
                messages.add_message( request,
                                      messages.ERROR,
                                      "Quantity cannot be zero")
            else:
                product.amount -= order.quantity
                product.save()
                order.save()
                messages.add_message( request,
                                      messages.SUCCESS,
                                      "Order created successfully")
                return redirect('product_detail', pk)

    context = {'product': product,
               'form': form,}
    return render(request, 'shop/detail.html', context)


@login_required
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'product/create.html', context)


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm()
    if request.method == 'POST':
        if form.is_valid():
            form = ProductForm(request.POST)
            product.name = form.cleaned_data['name'] if form.cleaned_data['name'] else product.name
            product.price = form.cleaned_data['price'] if form.cleaned_data['price'] else product.price
            product.description = form.cleaned_data['description'] if form.cleaned_data['description'] else product.description
            product.quantity = form.cleaned_data['amount'] if form.cleaned_data['amount'] else product.quantity
            product.image = form.cleaned_data['image'] if form.cleaned_data['image'] else product.image
            product.save()
        return redirect('home')  # Redirect to detail page

    return render(request, 'product/edit.html', {'form': form})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'product/delete.html', {'product': product})

def add_comment(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
        else:
            return 
        return redirect('product_detail', pk)
    return render(request, 'shop/detail.html', {'form': form})



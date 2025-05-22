from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    # product crud
    path('',views.index,name='index'),
    path('category/<int:category_id>/',views.index, name='products_by_category'),
    path('detail/<int:product_id>/',views.product_detail,name='product_detail'),
    path('product/create/',views.create_product,name='create_product'),
    path('product/delete/<int:pk>/',views.delete_product,name='delete_product'),
    # order logic
  
    path('order/detail/<int:pk>/',views.order_detail,name='order_detail'),
    path('comment/create/<int:pk>',views.comment_create,name='comment_create')
]


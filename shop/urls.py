from django.urls import path

from shop import views

urlpatterns = [
    path("", views.home, name="home"),
    path('detail/<int:product_id>/', views.product_detail, name="product_detail"),
    path('category/<category_title>', views.home, name="category_detail"),
    path('product/create/', views.create_product,name='create_product'),
    path('product/delete/<int:pk>/', views.delete_product,name='delete_product'),
    path('product/edit/<int:pk>/', views.edit_product,name='edit_product'),

    path('comment/add/<int:pk>/', views.add_comment,name='add_comment'),

    #order
    path('order/detail/<int:pk>', views.order_detail, name="order"),

]
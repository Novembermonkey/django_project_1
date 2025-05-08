from django.urls import path

from shop import views

urlpatterns = [
    path("", views.home, name="home"),
    path('detail/<int:product_id>/', views.product_detail, name="product_detail"),
    path('category/<category_title>', views.home, name="category_detail"),
]
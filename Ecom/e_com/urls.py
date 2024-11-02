from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    
    path('',views.home ,name='home'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:pk>', views.product_details, name='product_details'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('product/<int:pk>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart')
      

    
]

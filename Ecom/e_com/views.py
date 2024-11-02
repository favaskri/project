from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Cart
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 5)  # Cache for 2 minutes
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

# register

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= UserCreationForm()
    return render(request,'register.html',{'form':form})

            

# display product details
@login_required
def product_details(request,pk):
    product=get_object_or_404(Product,pk=pk)
    return render(request,'product_details.html',{'product':product})

@login_required
def cart_detail(request):
    # Get the cart for the current user
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart.html', {'cart': cart})

@login_required
def add_to_cart(request, pk):
    # Get the product by primary key (pk)
    product = get_object_or_404(Product, pk=pk)

    # Get or create a cart for the current user
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Add the product to the cart
    cart.products.add(product)

    # Redirect to cart detail page or render a template showing the cart
    return redirect('cart_detail')   

@login_required
def remove_from_cart(request, pk):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, pk=pk)
    cart.products.remove(product)
    return redirect('cart_detail')


# # adding a new product
@login_required
def add_product(request):
    if request.method =='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ProductForm()
    return render(request,'add_product.html',{'form':form})

# # Editing existing product
@login_required
def edit_product(request,pk):
    product= get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ProductForm(instance=product)
    
    return render(request,'edit_product.html',{'form':form})
# Deleting product

@login_required
def delete_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=="POST":
        product.delete()
        return redirect('home')
    return render(request,'edit_product.html',{'product':product})
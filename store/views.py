from django.shortcuts import render
from .models import Product
from django.contrib import messages
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


from django.shortcuts import get_object_or_404, redirect
from .models import Cart


from .models import Order

def checkout(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)

        for item in cart_items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity
            )

        cart_items.delete()

        messages.success(request, "Order placed successfully!")

    return redirect('/products/')

def products(request):
    search = request.GET.get('search', '').strip()

    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()

    return render(request, 'products.html', {'products': products})
from django.shortcuts import get_object_or_404, redirect
from .models import Cart, Product

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)

        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )

        messages.success(request, f"{product.name} added to cart successfully!")

    return redirect('/products/')



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        'product_detail.html',
        {'product': product}
    )



from .models import Wishlist

def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)

        Wishlist.objects.create(
            user=request.user,
            product=product
        )

        messages.success(request, f"{product.name} added to wishlist!")

    return redirect(f'/product/{product_id}/')


def buy_now(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)

        Order.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )

        messages.success(request, "Order placed successfully!")

    return redirect(f'/product/{product_id}/')



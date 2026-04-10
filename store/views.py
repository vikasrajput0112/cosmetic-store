from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def products(request):
    products = [
        {"id":1, "name":"Lipstick", "price":299},
        {"id":2, "name":"Face Cream", "price":499},
    ]
    return render(request, 'products.html', {"products": products})

def product_detail(request, id):
    product = {"id":id, "name":"Product", "price":299, "description":"Nice product"}
    return render(request, 'product_detail.html', {"product": product})

def cart(request):
    return render(request, 'cart.html', {"cart_items": [], "total": 0})

def checkout(request):
    return render(request, 'checkout.html')

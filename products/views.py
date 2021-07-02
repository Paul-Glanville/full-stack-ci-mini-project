from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view toe show all products, including sorting and search queries """

    products = product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "products/products.html", context)
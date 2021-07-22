from django.core import paginator
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
from cart.views import _cart_id
from cart.models import CartItem
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def store(request, category_slug =  None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = categories, is_available = True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available = True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products =paginator.get_page(page)
        products_count= products.count()


    context = {
        'products' : paged_products,
        'products_count':products_count
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        in_cart =  CartItem.objects.filter(cart__cart_id= _cart_id(request), product = single_product).exists()
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
        'in_cart':in_cart,
    }
    return render(request, 'store/product_detail.html', context)
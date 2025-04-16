from django.core.cache import cache
from .models import Product
from .serializers import ProductSerializer

def get_cached_products():
    cache_key = 'products_list'
    products = cache.get(cache_key)
    
    if not products:
        queryset = Product.objects.all().order_by('-id') # maybe get rid of the order_by for removing the latest entry highilihts
        serializer = ProductSerializer(queryset, many=True)
        products = serializer.data
        cache.set(cache_key, products, timeout=3600)
    
    return products

def invalidate_product_cache():
    cache.delete('products_list')
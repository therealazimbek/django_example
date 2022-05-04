from django.http import HttpResponse, JsonResponse
from .models import Product, Category


def homePage(request):
    return HttpResponse('API home')


def productsPage(request):
    products = [product.to_json() for product in Product.objects.all()]
    print(products)
    return JsonResponse(products, safe=False)


def product_detailsPage(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)
    return JsonResponse(product.to_json())    

def categoriesPage(request):
    categories = [category.to_json() for category in Category.objects.all()]
    return JsonResponse(categories, safe=False)


def category_detailsPage(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)
    return JsonResponse(category.to_json())


def category_products(request, pk):
    try:
        category = Category.objects.get(id=pk)
        products = [product.to_json() for product in Product.objects.filter(category=category)]
    except Category.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)
    except Exception as e:
        return JsonResponse({"message": "Something bad happened"}, status=500)    
    return JsonResponse(products, safe=False)

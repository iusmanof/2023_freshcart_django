from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
from . import models


def category_items(request, category, sub_category):
    if category == 'food':

        match sub_category:
            case 'bakery':
                sub_category_name = models.SubCategory.objects.get(id=1)
                sub_category_products = models.Product.objects.filter(subcategory=1)
                context = {'name': sub_category_name, 'list': sub_category_products }
            case 'desserts':
                sub_category_name = models.SubCategory.objects.get(id=1)
                sub_category_products = models.Product.objects.filter(subcategory=2)
                context = {'name': sub_category_name, 'list': sub_category_products }
            case 'drinks':
                sub_category_name = models.SubCategory.objects.get(id=1)
                sub_category_products = models.Product.objects.filter(subcategory=3)
                context = {'name': sub_category_name, 'list': sub_category_products}
            case default:
                return HttpResponseNotFound("Sub_category not found. CAll us and we create it...")
        return render(request, 'category/index.html', context)

    return HttpResponseNotFound("Category not found")

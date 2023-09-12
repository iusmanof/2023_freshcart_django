from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
def category_items(request, category, sub_category):
    if category == 'food':

        match sub_category:
            case 'bakery':
                context = {'list': ['Baguette', 'Biscuits', 'Bread', 'Bread Loaf', 'Bread and Rolling Pin', 'Brezel', 'Gingerbread House', 'Merry Pie', 'Naan' , 'Pretzel']}
            case 'desserts':
                context = {'list': ['Apple Jam', 'Banana Split', 'Cheesecake', 'Cherry Cheesecake', 'Chocolate Bar', 'Chocolate Truffle', 'Ice Cream Cone' , 'Jam']}
            case 'drinks':
                context = {'list': ['Coconut Milk', 'Hemp Milk', 'Juice Bottle', 'Oat Milk', 'Orange Soda', 'Soda Water', 'The Toast']}
            case default:
                return HttpResponseNotFound("Sub_category not found. CAll us and we create it...")
        return render(request, 'category/index.html', context)



    return HttpResponseNotFound("Category not found")

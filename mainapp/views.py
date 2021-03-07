from django.shortcuts import render

from mainapp.models import ProductCategory, Product


# функции = вьюхи = контроллеры
def index(request):
    context = {'title': 'GeekShop',
               'descriptoins':'Новые образы и лучшие бренды на GeekShop Store.\nБесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'}
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)

from django.shortcuts import render
from datetime import datetime


# функции = вьюхи = контроллеры
def index(request):
    context = {'title': 'GeekShop',
               'descriptoins':'Новые образы и лучшие бренды на GeekShop Store.\nБесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'GeekShop - Каталог',
               'products_menu': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
               'products': [
                   {
                       'img': 'vendor/img/products/Adidas-hoodie.png',
                       'title': 'Худи черного цвета с монограммами adidas Originals',
                       'price': '6 090,00',
                       'descriptions': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
                   },
                   {
                       'img': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                       'title': 'Синяя куртка The North Face',
                       'price': '23 725,00',
                       'descriptions': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
                   },
                   {
                       'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                       'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                       'price': '3 390,00',
                       'descriptions': 'Материал с плюшевой текстурой. Удобный и мягкий.'
                   },
                   {
                       'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                       'title': 'Черный рюкзак Nike Heritage',
                       'price': '2 340,00',
                       'descriptions': 'Плотная ткань. Легкий материал.'
                   },
                   {
                       'img': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                       'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                       'price': '13 590,00',
                       'descriptions': 'Гладкий кожаный верх. Натуральный материал.'
                   },
                   {
                       'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                       'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                       'price': '2 890,00',
                       'descriptions': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
                   }
               ]
               }
    return render(request, 'mainapp/products.html', context)


def test_context(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00'},
        ],
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00'},
        ]
    }
    return render(request, 'mainapp/test-context.html', context)

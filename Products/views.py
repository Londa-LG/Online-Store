from django.shortcuts import render
from .models import Product , Review, About

# Create your views here.
def home(request):
    first = Product.objects.exclude(id=4).exclude(id=5).exclude(id=6).exclude(id=7).exclude(id=8).exclude(id=9)
    second = Review.objects.all()
    content = {"products01": first,
               "reviews": second,
               }
    return render(request,'Products/home.html',content)

def product_page(request,id):
    context = {"product": Product.objects.filter(id=id)}
    return render(request,'Products/product_page.html',context)

def about(request):
    return render(request,'Products/about.html',{"about": About.objects.all})

def product(request):
    pro01= Product.objects.exclude(id=4).exclude(id=5).exclude(id=6).exclude(id=7).exclude(id=8).exclude(id=9)
    pro02 = Product.objects.exclude(id=1).exclude(id=2).exclude(id=3).exclude(id=7).exclude(id=8).exclude(id=9)
    pro03 = Product.objects.exclude(id=1).exclude(id=2).exclude(id=3).exclude(id=4).exclude(id=5).exclude(id=6)
    content={ "products01": pro01,
              "products02": pro02,
              "products03":pro03
    }
    return render(request,'Products/products.html',content)
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from .models import BuyProperty
from .models import Category
from account import views
from account.models import User
# Create your views here.


#==all-post(Home)==========#
def allproperty(request):
    User == 'user'
    buyproperty = BuyProperty.objects.all().order_by('-pk')
    city = BuyProperty.objects.values('city').distinct()
    category = Category.objects.values('name','id').distinct()
    context = {'buyproperty': buyproperty,'city':city, 'category':category}
    return render(request, 'properties/property.html', context)

#==all-Lease==========#
def alllease(request):
    User == 'user'
    buyproperty = BuyProperty.objects.filter(category='3')
    city = BuyProperty.objects.values('city').distinct()
    category = Category.objects.values('name','id').distinct()
    context = {'buyproperty': buyproperty,'city':city, 'category':category}
    return render(request, 'properties/property.html', context)


#==all-rent==========#
def allrent(request):
    User == 'user'
    buyproperty = BuyProperty.objects.filter(category='2')
    city = BuyProperty.objects.values('city').distinct()
    category = Category.objects.values('name','id').distinct()
    context = {'buyproperty': buyproperty,'city':city, 'category':category}
    return render(request, 'properties/property.html', context)


#==Property-Post-Page================#
def propertypost(request, slug):
    post = BuyProperty.objects.filter(slug=slug).first()
    allproperty = BuyProperty.objects.all()
    context = {'allproperty': allproperty,'post':post}
    return render(request, 'properties/property-post.html', context)

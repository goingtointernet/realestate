from django.shortcuts import redirect, render
from account.forms import SignUPForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from properties.models import BuyProperty
from properties.models import Category
from django.db.models import Q
from .models import StaticPosts
from django.core.mail import send_mail
from django.contrib import messages
from advertisement.models import AdsProperty
# Create your views here.
#==home==========================#
def index(request):
    buyproperty = BuyProperty.objects.all().order_by('-pk')
    ads = AdsProperty.objects.all().order_by('-pk')
    rentproperty = BuyProperty.objects.filter(category=2).order_by('-pk')
    leaseproperty = BuyProperty.objects.filter(category=4).order_by('-pk')
    print(leaseproperty)
    city = BuyProperty.objects.values('city').distinct()
    category = Category.objects.values('name','id').distinct()
    context = {'buyproperty': buyproperty,'ads':ads ,'rentproperty':rentproperty,'leaseproperty':leaseproperty,'city':city, 'category':category}
    return render(request, 'index.html', context)


#==Register==============================#
def register(request):
    msg = None
    
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = SignUPForm(request.POST)
            email = request.POST.get('email')
            password1 = request.POST.get('password1')

            if form.is_valid():
                form.save()
                msg = 'user created'
                data = {
                    'email':email,
                    'password1':password1
                }
                message = '''
                Welcome To Real Estate Advisor System,
                
                Your Email Is: {}
                Your Password Is: {}
                '''.format(data['email'],data['password1'])
                send_mail('Real Estate Advisor System', message, '',[email])
                return redirect('login_view')
            else:
                msg = 'form is not valid'
        else:
            form = SignUPForm()
        return render(request, 'signup.html', {'form': form, 'msg': msg})
    
    elif request.user.is_authenticated:
        return redirect('index')



#==login=============================#
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    
    if request.user.is_anonymous:    
        if request.method =='POST':
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                
                if user and not user.is_active:
                    msg= '*Account is Deactivated'

                elif user and user.is_active:
                    login(request, user)
                    return redirect('index')

                else:
                    msg= '* Invalid Credentials'
            else:
                msg = 'Error Valitation form'
        return render(request, 'login.html',{'form':form, 'msg':msg})
    elif request.user.is_authenticated:
        return redirect('index')


#==logout===============================#
def logoutUser(request):
    logout(request)
    return redirect('index')

#==404==================================#
def page_not_found(request,  exception):
    return render(request, '404.html', status=404)

#==Call-Request=========================#
def callrequest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        message = '''
        New Message:{}

        Name:{}
        Phone:{}
        Email:{}
        '''.format(data['message'],data['name'],data['phone'],data['email'])
        send_mail('Call Request', message, '',['touseeqijazpro1@gmail.com'])
        messages.success(request, '*Sent Successfully')
    return redirect('index')


#==Search============================#
def search(request):
    city=request.GET['city']
    category=request.GET['category']

    if request.GET['maxprice'] == '':
        maxprice=10000000000
    else:    
        maxprice=request.GET['maxprice']

    filters = Q(Q(category=category) & Q(city=city) &  Q(monthly_instalment__lte=maxprice) & Q(property_price__lte=maxprice) )
    buyproperty = BuyProperty.objects.filter(filters)

    city = BuyProperty.objects.values('city').distinct()
    category = Category.objects.values('name','id').distinct()


    params={'buyproperty': buyproperty,'city':city, 'category':category}
    return render(request, 'home/search.html', params)

#==Static-post============================#
def staticpost(request,slug):
    staticpost = StaticPosts.objects.filter(slug=slug).first()
    allpost = StaticPosts.objects.all()
    context = {'allpost': allpost,'staticpost':staticpost}
    return render(request, 'home/static-post.html', context)    


#==Contact-Page==========================#
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email':email,
            'message':message,
        }
        message = '''
        New Message:{}

        From:{}
        '''.format(data['message'],data['email'])
        send_mail(data['name'], message, '',['touseeqijazpro1@gmail.com'])
        messages.success(request, '*Sent Successfully')
    return render(request, 'home/contact.html')
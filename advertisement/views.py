from django.http import HttpResponse
from django.shortcuts import render
from .models import AdsProperty
#==Advertisement-Home=====================#
def all_advertisement(request):
    ads = AdsProperty.objects.all()
    context = {'buyproperty': ads}
    return render(request, 'properties/property.html', context)

#==ad-Post==============================#
def adpost(request, slug):
    post = AdsProperty.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'ads/ad-post.html', context)

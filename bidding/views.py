from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Lot, BiddingParticipator
from django.utils import timezone
from django.db.models import Max


# Create your views here.


#==All-Bidding==============================#
def all_bidding(request):
    bidding = Lot.objects.all().order_by('-pk')
    context = {'bidding': bidding,}
    return render(request, 'bidding/bidding.html', context)

#==Bidding-Post================#
def bidding_post(request, slug):
    post = Lot.objects.filter(slug=slug).first()
    allproperty = Lot.objects.all()
    bidding_participate = BiddingParticipator.objects.filter(item = post.id).order_by('-pk')
    bidding_participate_count = BiddingParticipator.objects.filter(item = post.id).count()
    current_datetime = timezone.now()
    
    if bidding_participate_count == 0:
       min_value = post.bidding_start_price + 1
       top_bidder = None
    else:
        top_bidder = BiddingParticipator.objects.filter(item = post.id).last()
        min_value = top_bidder.bidding_price + 1 

    
    if request.user.is_authenticated:
        if request.method=="POST":
            paricipator = request.POST.get('paricipator')
            paricipator  = request.user
            item_id = request.POST.get('item')
            item = Lot.objects.get(id = item_id)
            bidding_price = request.POST.get('bidding_price')
            bidingpart = BiddingParticipator(paricipator=paricipator,item=item, bidding_price=bidding_price) 
            bidingpart.save()
            return redirect( 'bidding_post', slug)
        else:
            pass
    else:
        return redirect('login_view')
    context = {'allproperty': allproperty,'post':post, 'current_datetime':current_datetime ,'bidding_participate':bidding_participate, 'min_value':min_value, 'top_bidder':top_bidder}
    return render(request, 'bidding/bidding-post.html', context)


#==My-bidding-list===============#
def my_bidding_list(request):
    if request.user.is_authenticated:
        bidding_participate = BiddingParticipator.objects.filter(paricipator = request.user.id).order_by('-pk')
        highbider = Lot.objects.annotate(
            highest_bid=Max('biddingparticipator__bidding_price')
            )

        current_datetime = timezone.now()
        
        context = {'bidding_participate':bidding_participate, 'highbider':highbider, 'current_datetime':current_datetime}
        return render(request, 'bidding/my-bidding-list.html', context)
    else:
        return redirect('login_view')
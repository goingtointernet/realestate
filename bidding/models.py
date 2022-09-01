from django.db import models
from datetime import datetime
from account.models import User
from properties.models import Category

#==Bidding Model=======================#
class Lot(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    slug = models.CharField(max_length=70, unique=True)
    content = models.TextField()
    property_img1 = models.ImageField( upload_to = 'static/images/bidding', null = True, blank = True)
    property_img2 = models.ImageField( upload_to = 'static/images/bidding', null = True, blank = True)
    property_img3 = models.ImageField( upload_to = 'static/images/bidding', null = True, blank = True)
    thumbnail = models.ImageField( upload_to = 'static/images/bidding', null = True, blank = True)
    bidding_start_price = models.IntegerField(default=0)
    address = models.CharField(max_length=240)
    city = models.CharField(max_length=240,default='')
    room = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    kitchen = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    marla = models.FloatField(max_length=4,default=0.0)
    is_live=models.BooleanField(default=False)
    on_banner=models.BooleanField(default=False)
    end_bidding =  models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title + ' | ' + str(self.bidder)
    


#==Bidding Participator Model=======================#
class BiddingParticipator(models.Model):
    paricipator = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Lot, on_delete=models.CASCADE, default=True, null=False)
    bidding_price = models.IntegerField()
    bidding_time = models.DateTimeField(default=datetime.now())
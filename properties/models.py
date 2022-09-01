from django.db import models
from account.models import User

# Create your models here.

#Category
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#Buy Property Model
class BuyProperty(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    content = models.TextField()
    slug = models.CharField(max_length=70, unique=True)
    property_img1 = models.ImageField( upload_to = 'static/images/property', null = True, blank = True)
    property_img2 = models.ImageField( upload_to = 'static/images/property', null = True, blank = True)
    property_img3 = models.ImageField( upload_to = 'static/images/property', null = True, blank = True)
    thumbnail = models.ImageField( upload_to = 'static/images/property', null = True, blank = True)
    property_price = models.IntegerField(default=0)
    monthly_instalment = models.IntegerField(default=0)
    advance = models.IntegerField(default=0)
    lease_complete_in_years = models.IntegerField(default=0)
    address = models.CharField(max_length=240)
    city = models.CharField(max_length=240,default='')
    room = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    kitchen = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    marla = models.FloatField(max_length=4,default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
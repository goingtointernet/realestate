from django.urls import path
from . import views


urlpatterns = [
    path('',views.all_bidding, name='all_bidding'),
    path('my-list',views.my_bidding_list, name='my_bidding_list'),
    path('<str:slug>',views.bidding_post, name='bidding_post'),
]
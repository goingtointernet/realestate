from django.urls import path
from . import views


urlpatterns = [
    path('',views.all_advertisement, name='all_advertisement'),
    path('<str:slug>',views.adpost, name='adpost'),
]
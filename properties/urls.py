
from django.urls import path
from . import views


urlpatterns = [
    path('',views.allproperty, name='allproperty'),
    path('lease',views.alllease, name='alllease'),
    path('rent',views.alllease, name='allrent'),
    path('<str:slug>',views.propertypost, name='propertypost'),
]
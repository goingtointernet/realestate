
from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile_view, name='profile_view'),
    path('changepassword',views.userchangepass, name='userchangepass'),
]

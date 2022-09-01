from django.shortcuts import redirect, render
from .forms import EditUserProfileForm
from django.contrib.auth import update_session_auth_hash
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


#==Profile========================#
def profile_view(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = EditUserProfileForm(request.POST,request.FILES, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, '*Profile Update Successfully')
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request,'profile.html',{'form':fm})
    else:
        return render(request,'404.html')



#==Change-User-Password============================#
def userchangepass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            ps = PasswordChangeForm(user=request.user, data=request.POST)
            if ps.is_valid():
                ps.save()
                update_session_auth_hash(request, ps.user)
                messages.success(request, '*Password Change Successfully')
                return redirect('profile_view')
        else:
            ps = PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'form2':ps})
    else:
        return render(request,'404.html')



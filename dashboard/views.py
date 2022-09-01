import imp
from unicodedata import category
from home.models import StaticPosts
from django.contrib import messages
from django.shortcuts import redirect, render
from properties.models import Category
from properties.models import BuyProperty
from django.views.generic import UpdateView, CreateView, DeleteView
from home.models import FooterData
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from account.models import User
from advertisement.models import AdsProperty
from bidding.models import Lot, BiddingParticipator
from dashboard.models import DashReports
# Create your views here.


#==Dashboard-home====================#
def dashboard(request):
    if request.user.is_anonymous or request.user.is_buyer:
        return render(request, '404.html')
    else:
        return render(request, 'dashboard/dashboard.html')
#==Reports====================#
def reports(request):
    if request.user.is_anonymous or request.user.is_buyer:
        return render(request, '404.html')
    else:
        reports = DashReports.objects.all().first()
        return render(request, 'dashboard/reports.html', {'reports': reports})
#==Property-Ads===================#
class CreateAdvertisement(SuccessMessageMixin, CreateView):
    model = AdsProperty
    fields = '__all__'
    success_url = reverse_lazy('all_ads')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/create-property-ad.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs)

    success_message = "*advertisement Create Successfully*"  

#==All-Ads=========================#
def all_ads(request):
    if request.user.is_anonymous or request.user.is_buyer or request.user.is_seller:
        return render(request, '404.html')
    else:
        propertyads = AdsProperty.objects.all()
        context = {'propertyads': propertyads}
        return render(request, 'dashboard/all-ads.html', context)

#==Edit-Advertisment=========================#
class EditAds(SuccessMessageMixin, UpdateView):
    model = AdsProperty
    fields = ['title','category','content','marla','thumbnail','monthly_instalment', 'property_price', 'advance', 'lease_complete_in_years', 'property_img1','property_img2','property_img3','address','city','room','bathroom','kitchen','floor']
    success_url = reverse_lazy('all_ads')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/edit-ads.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs)

    success_message = "*Ad Update Successfully*"

#==Delete-Category==============#
class DeleteAds(SuccessMessageMixin, DeleteView):
    model = AdsProperty
    success_url = reverse_lazy('all_ads')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/delete-ad.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs) 

    success_message = "*Ad Delete Successfully*"  

#==Create-Post=====================#
class CreatePost(SuccessMessageMixin, CreateView):
    model = BuyProperty
    fields = '__all__'
    success_url = reverse_lazy('all_posts')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser or request.user.is_seller:
            self.template_name = 'dashboard/create-post.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs)

    success_message = "*Post Create Successfully*"

#==All-post=========================#
def all_posts(request):
    if request.user.is_anonymous or request.user.is_buyer:
        return render(request, '404.html')
    else:
        buyproperty = BuyProperty.objects.all()
        context = {'buyproperty': buyproperty}
        return render(request, 'dashboard/all-posts.html', context)


#==Edit-post=========================#
class EditPost(SuccessMessageMixin, UpdateView):
    model = BuyProperty
    fields = ['title','category','content','marla','thumbnail','monthly_instalment', 'property_price', 'advance', 'lease_complete_in_years', 'property_img1','property_img2','property_img3','address','city','room','bathroom','kitchen','floor']
    success_url = reverse_lazy('all_posts')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser or request.user.is_seller:
            self.template_name = 'dashboard/edit-post.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs)

    success_message = "*Post Update Successfully*"

#==All-Pages=========================#
def all_pages(request):
    if request.user.is_anonymous or request.user.is_buyer or request.user.is_seller:
        return render(request, '404.html')
    else:
        post = StaticPosts.objects.all()
        context = {'post': post}
        return render(request, 'dashboard/all-pages.html', context)


#==Create-Page=========================#
class CreatePage(SuccessMessageMixin, CreateView):
    model = StaticPosts
    fields = '__all__'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/create-page.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs)

    success_message = "*Page Create Successfully*"  

#==Edit-Page=========================#
class EditPage(SuccessMessageMixin, UpdateView):
    model = StaticPosts
    fields = ['title','page_name','content']
    success_url = reverse_lazy('all_pages')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/edit-page.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs)  

    success_message = "*Page Update Successfully*"
    


#==Edit-Footer=========================#
class EditFooter(SuccessMessageMixin, UpdateView):
    model = FooterData
    fields = '__all__'

    success_url = reverse_lazy('dashboard')
    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/edit-footer.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs) 

    success_message = "*Footer Update Successfully*"
#==Edit-Reports=========================#
class Reports(SuccessMessageMixin, UpdateView):
    model = DashReports
    fields = '__all__'

    success_url = reverse_lazy('reports')
    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/edit-reports.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs) 

    success_message = "*Reports Update Successfully*"


#==Clients====================#
def all_clients(request):
    if request.user.is_anonymous or request.user.is_buyer or request.user.is_seller:
        return render(request, '404.html')
    else:
        client = User.objects.all()
        context = {'client': client}
        return render(request, 'dashboard/clients.html', context)

#==change-User-Status=================#
class EditUserStatus(SuccessMessageMixin, UpdateView):
    model = User
    fields = ['is_active','first_name','last_name','username','email','phone','bio','is_superuser']

    success_url = reverse_lazy('all_clients')   

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/edit-client.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs) 
    
    success_message = "*User Update Successfully*" 


#==Delete-post==============#
class DeletePost(SuccessMessageMixin, DeleteView):
    model = BuyProperty
    success_url = reverse_lazy('all_posts')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/delete-post.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs) 

    success_message = "*Post Delete Successfully*"   

#==Delete-page==============#
class DeletePage(SuccessMessageMixin, DeleteView):
    model = StaticPosts
    template_name = 'dashboard/delete-page.html'
    success_url = reverse_lazy('all_pages')
    success_message = "*Page Delete Successfully*"   

#==Delete-Bid==============#
class DeleteBid(SuccessMessageMixin, DeleteView):
    model = Lot
    success_url = reverse_lazy('d_all_bidding')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/delete-bid.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs) 

    success_message = "*Bidding Post Delete Successfully*"   

#==All-Category=========================#
def all_category(request):
    if request.user.is_anonymous or request.user.is_buyer or request.user.is_seller:
        return render(request, '404.html')
    else:
        category = Category.objects.all()
        context = {'category': category}
        return render(request, 'dashboard/all-category.html', context)

#==Delete-Category==============#
class DeleteCategory(SuccessMessageMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('all_category')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/delete-category.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs) 

    success_message = "*Category Delete Successfully*"  

#==Edit-Category=========================#
class EditCategory(SuccessMessageMixin, UpdateView):
    model = Category
    fields = '__all__'

    success_url = reverse_lazy('all_category')
    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/edit-category.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs) 

    success_message = "*Category Update Successfully*"



#==Create-Category=========================#
class CreateCategory(SuccessMessageMixin, CreateView):
    model = Category
    fields = '__all__'

    success_url = reverse_lazy('all_category')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/create-category.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs)

    success_message = "*Category Create Successfully*"  



#==All-Ads=========================#
def d_all_bidding(request):
    if request.user.is_anonymous or request.user.is_buyer:
        return render(request, '404.html')
    else:
        bidding = Lot.objects.all()
        context = {'bidding': bidding}
        return render(request, 'dashboard/all-bidding.html', context)
#==All-Participator=========================#
def d_all_paricipator(request, slug):
    if request.user.is_anonymous or request.user.is_buyer:
        return render(request, '404.html')
    else:
        post = Lot.objects.filter(slug=slug).first()
        bidding_participate = BiddingParticipator.objects.filter(item = post.id).order_by('-pk')
        context = {'bidding_participate': bidding_participate}
        return render(request, 'dashboard/all-participator.html', context)

#==Create-Bid=========================#
class CreateBid(SuccessMessageMixin, CreateView):
    model = Lot
    fields = '__all__'

    success_url = reverse_lazy('d_all_bidding')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_seller or request.user.is_admin or request.user.is_superuser:
            self.template_name = 'dashboard/create-bid.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs)

    success_message = "*Bid Create Successfully*"  

#==Edit-Bid=========================#
class EditBid(SuccessMessageMixin, UpdateView):
    model = Lot
    fields = '__all__'

    success_url = reverse_lazy('d_all_bidding')
    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser or request.user.is_seller:
            self.template_name = 'dashboard/edit-bid.html'
        else:
            self.template_name = '404.html'
        return super().dispatch(request, *args, **kwargs) 

    success_message = "*Bid Update Successfully*"


from django.urls import path
from .views import EditBid, EditPost, EditPage, CreatePage, EditFooter, EditUserStatus, DeletePost, DeletePage, CreatePost, DeleteCategory, EditCategory, CreateCategory, CreateAdvertisement, EditAds, DeleteAds, DeleteBid, CreateBid, EditBid, Reports
from . import views


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('create-post',CreatePost.as_view(), name='create_post'),
    path('all-posts',views.all_posts, name='all_posts'),
    path('all-bidding',views.d_all_bidding, name='d_all_bidding'),
    path('all-pages',views.all_pages, name='all_pages'),
    path('all-category',views.all_category, name='all_category'),
    path('clients',views.all_clients, name='all_clients'),
    path('advertisement',views.all_ads, name='all_ads'),
    path('reports',views.reports, name='reports'),
    path('participator/<str:slug>',views.d_all_paricipator, name='d_all_paricipator'),
    path('advertisement/property/create',CreateAdvertisement.as_view(), name='property_advertisement'),
    path('create-page',CreatePage.as_view(), name='create_page'),
    path('create-bid',CreateBid.as_view(), name='create_bid'),
    path('create-category',CreateCategory.as_view(), name='create_category'),
    path('edit-footer/<int:pk>', EditFooter.as_view(), name='edit_footer'),
    path('edit-report/<int:pk>', Reports.as_view(), name='edit_reports'),
    path('edit-category/<int:pk>', EditCategory.as_view(), name='edit_category'),
    path('edit-post/<str:slug>', EditPost.as_view(), name='edit_post'),
    path('edit-bid/<str:slug>', EditBid.as_view(), name='edit_bid'),
    path('advertisement/edit/<str:slug>', EditAds.as_view(), name='edit_ads'),
    path('edit-page/<str:slug>', EditPage.as_view(), name='edit_page'),
    path('user/<int:pk>', EditUserStatus.as_view(), name='edit_user'),
    path('post/<str:slug>/delete', DeletePost.as_view(), name='delete_post'),
    path('Bid/<str:slug>/delete', DeleteBid.as_view(), name='delete_bid'),
    path('page/<str:slug>/delete', DeletePage.as_view(), name='delete_page'),
    path('advertisement/delete/<str:slug>', DeleteAds.as_view(), name='delete_ads'),
    path('category/<int:pk>/delete', DeleteCategory.as_view(), name='delete_category')
]
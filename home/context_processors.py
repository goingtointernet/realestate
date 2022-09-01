from django.conf import settings
from .models import StaticPosts,FooterData

#Static-Page-Post
def staticposts(request):
    staticposts = StaticPosts.objects.all()
    return {"staticposts": staticposts}

#Footer Data
def footerdata(request):
    footerdata = FooterData.objects.all()[0]
    return {"footerdata": footerdata}
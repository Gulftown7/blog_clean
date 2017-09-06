from django.contrib.sites import requests
from django.http.response import HttpResponse


# Create your views here.
def post_home(request):
    
    return HttpResponse("<h1>Title</h1>")

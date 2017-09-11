
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404



# Create your views here.

from posts.models import Post


def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    instance = get_object_or_404(Post, id=2)
    context = {
        "title": "Post detail",
        "instance": instance,
    }
    return render(request, "post_detail.html", context)
    

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "Post list"
    }
#     if request.user.is_authenticated():
#         context = {
#             "title": "User is authenticated. Template works!"
#         }
#     else:
#         context = {
#             'title': 'Not authenticated. Template not works.'
#         }       
    return render(request, "index.html", context)
#     return HttpResponse("<h1>List</h1>")

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")

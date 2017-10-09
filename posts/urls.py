from django.conf.urls import url


from posts import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/edit/$', views.post_update, name='post_update'),
    url(r'^(?P<post_id>\d+)/delete/$', views.post_delete, name='post_delete'),  
]
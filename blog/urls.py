from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/create$',views.PostCreateView.as_view(),name='create'),
    url(r'^post/update/(?P<pk>\d+)$',views.PostUpdateView.as_view(),name='update'),
    url(r'^post/delete/(?P<pk>\d+)$',views.PostDeleteView.as_view(),name='delete'),
    url(r'^post/(?P<pk>\d+)/publish$',views.post_publish,name='post_publish'),
    url(r'^drafts$',views.DraftListView.as_view(),name='drafts'),
    url(r'^post/(?P<pk>\d+)/comments$',views.add_comment_to_post,name='add_comment'),
    url(r'^comment/(?P<pk>\d+)/approve$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/delete$',views.comment_delete,name='comment_delete'),



]

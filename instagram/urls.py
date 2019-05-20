from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ImageCreateView,ImageListView,ImageDetailView,UserImageListView,ImageUpdateView,ImageDeleteView,CommentCreateView


urlpatterns=[
    url(r'^$', ImageListView.as_view(), name = 'instagram-home'),
    # url(r'^user/(?P<username>\w+)/$',UserImageListView.as_view(), name='user-posts'),
    # url(r'^post/(?P<username>\w+)/$',UserImageListView.as_view(), name='user-posts'),
    url(r'^post/(?P<username>\w+)/$', UserImageListView.as_view(), name='user-posts'),
    url(r'^post/new/$',ImageCreateView.as_view(), name='image-create'),
    url(r'^post/(?P<pk>\d+)/comment/$',CommentCreateView.as_view(), name='comment-create'),
    url(r'^image/(?P<pk>\d+)/',ImageDetailView.as_view(), name='image-detail'),
    url(r'^about/', views.about, name = 'instagram-about'),
    url(r'^post/(?P<pk>\d+)/update/',ImageUpdateView.as_view(), name='image-update'),
    url(r'^post/(?P<pk>\d+)/delete/',ImageDeleteView.as_view(), name='image-delete'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
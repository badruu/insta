from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ImageCreateView,ImageListView,ImageDetailView,UserImageListView,ImageUpdateView,ImageDeleteView,CommentCreateView


urlpatterns=[
    url(r'^$', ImageListView.as_view(), name = 'instagram-home'),
    url(r'^post/new/$',ImageCreateView.as_view(), name='image-create'),
    url(r'^post/(?P<username>\w+)/$', UserImageListView.as_view(), name='user-posts'),
    url(r'^post/(?P<pk>\d+)/up-vote/$', views.image_up_vote, name='image_up_vote'),
    url(r'^post/(?P<pk>\d+)/down-vote/$', views.image_down_vote, name='image_down_vote'),
    url(r'^post/(?P<pk>\d+)/comment/$',CommentCreateView.as_view(), name='comment-create'),
    url(r'^image/(?P<pk>\d+)/',ImageDetailView.as_view(), name='image-detail'),
    url(r'^about/', views.about, name = 'instagram-about'),
    url(r'^post/(?P<pk>\d+)/update/',ImageUpdateView.as_view(), name='image-update'),
    url(r'^post/(?P<pk>\d+)/delete/',ImageDeleteView.as_view(), name='image-delete'),
    url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# SOME NOTES
# IF imagelistview comes b4 imagecreateview, error 404 of the url not found is portrayed.
# ACTUAL ERROR
# Page not found (404)
# Request Method:	GET
# Request URL:	http://localhost:8000/post/new/
# Raised by:	instagram.views.UserImageListView
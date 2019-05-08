from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^prof$',views.prof,name='prof'),
    url(r'^post$',views.post,name='post'),
    url(r'^search$',views.search,name='search'),
    url(r'^new_prof$',views.new_prof,name='new_prof'),
    url(r'^new_post$',views.new_post,name='new_post'),
    url(r'^delete/<id>/(\d+)$',views.delete,name='delete'),
    url(r'^new_comment$',views.new_comment,name='new_comment'),
    url(r'^admin/$',views.admin,name='admin'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

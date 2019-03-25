from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.all_images,name='home'),
url(r'^profile/$',views.prof,name='prof'),
url(r'^new_img$',views.new_img,name='new_img'),
url(r'^edit_prof$',views.edit_prof,name='edit_prof'),
url(r'^admin/$',views.admin,name='admin'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

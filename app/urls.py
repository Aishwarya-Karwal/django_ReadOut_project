from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
#from django.conf.urls import url 

urlpatterns = [
    path('',views.index, name='index') ,
    path('result', views.result , name = 'result'),
    

]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

'''
url(r'^media/(?P<path>.*)$',serve, {'document_root':settings.MEDIA_ROOT}),
url(r'^static/(?P<path>.*)$',serve, {'document_root':settings.STATIC_ROOT}),

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
'''
# print(static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT))

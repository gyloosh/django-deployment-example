from django.conf.urls import url
from . import views


#TEMPLATE TAGGIN
app_name = 'basic_app' # to jest template tagging, czyli dzięki temu w pliku
# html nie będzie trzeba na twardo kodować adresów stron

urlpatterns= [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),

]

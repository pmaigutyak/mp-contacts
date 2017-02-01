
from django.conf.urls import url

from contacts import views


urlpatterns = [

    url(r'^$', views.index, name='index'),

]

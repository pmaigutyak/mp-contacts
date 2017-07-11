
from django.conf.urls import url

from contacts import views


urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^return-call/$', views.create_return_call, name='return-call'),

    url(r'^error-message/$', views.create_error_message, name='error-message'),

]

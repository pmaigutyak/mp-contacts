
from django.urls import path

from contacts.return_calls import views


app_name = 'return-calls'


urlpatterns = [

    path('', views.CreateReturnCallView.as_view(), name='create'),

]


from django.urls import path

from contacts.feedback import views


app_name = 'feedback'


urlpatterns = [

    path('', views.CreateFeedbackView.as_view(), name='create'),

]

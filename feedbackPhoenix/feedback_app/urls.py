from django.conf.urls import url
from feedback_app import views

urlPattern = [
    url(r'^$', views.index, name='index'),
    url(r'help', views.help, name='help'),
    url(r'feedback', views.feedback, name='feedback'),
]

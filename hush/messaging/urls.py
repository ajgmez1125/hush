from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('start-conversation', views.startconversation, name='start-conversation'),
    path('sendmessage',views.sendmessage, name='sendmessage'),
    path('join-conversation/<int:pk>', views.joinconversation, name='join-conversation'),
    path('hello-world', views.helloworld, name='hello-world')
]
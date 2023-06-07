from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('<str:room>/',views.room,name='room'),#Add / after completing <> for variable url
    path('checkroom',views.checkroom,name='checkroom'),
    path('send',views.send,name='send'),
    #order of the urls is important for redirecting
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
]

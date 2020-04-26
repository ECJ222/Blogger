from django.urls import path,include
from main import views as v
from user import views as vi
urlpatterns=[
   path('',v.blog,name='blog'),
   path('about/',v.about,name='about'),
   path('contact/',v.contact,name='contact'),
   path('',v.logoutt,name='logout')
]
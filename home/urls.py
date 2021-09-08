from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path('', views.index, name ='home'),
   path("index.html", views.index, name ='index'),
   path("about.html", views.about, name ='about'),
   path("contact.html", views.contact, name ='contact'),
   path("post.html", views.post, name ='post'),
   path("post2.html", views.post2, name ='post2'),
   path("post3.html", views.post3, name ='post3')
   
]
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('post/<slug:slug>',views.post_page,name='post_page'),
    
]
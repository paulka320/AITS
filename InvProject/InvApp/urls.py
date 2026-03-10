from django.urls import path
from . import views

urlpatterns =[
path('',views.index),
path('about/',views.about ,name='about'),
path('element/',views.element ,name='element'),
path('welcome/',views.contact_view ,name='welcome'),
path('Home/',views.home_view,name='home'),
]

from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personalrecord', views.personalrecord, name='personalrecord'),
    path('educatipn', views.education, name='education'),
    path('interests', views.interests, name='interests'),
    path('product', views.product, name='product'),
    path('rolemodel', views.rolemodel, name='rolemodel'),
    path('showMyData', views.showMyData, name='showMyData'),

]

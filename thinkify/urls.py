from django.urls import path
from .import views

app_name='thinkify'
urlpatterns =[
    path('', views.home.as_view(),name='Home'),
    path('loginPage', views.LoginPage.as_view(), name='loginPage'),
    path('registerPage',views.registerPage.as_view(),name='registerPage'),
    path('home', views.homeNext.as_view(),name='homeNext'),
    path('logout', views.Logout.as_view(),name='logout'),
    path('Agri_Modernisation',views.Agri_Modernisation.as_view(),name='Agri_Modernisation'),
    path('Agri_Resources',views.Agri_Resources.as_view(),name='Agri_Resources'),
    path('AI_Drones',views.AI_Drones.as_view(),name='AI_Drones'),
    path('contact',views.contact.as_view(),name='contact'),
    path('Estimate',views.Estimate.as_view(),name='Estimate'),
    path('Legal',views.Legal.as_view(),name='Legal'),
    path('Malware',views.Malware.as_view(),name='Malware'),
    path('Robotics',views.Robotics.as_view(),name='Robotics'),
    path('Rural', views.Rural.as_view(), name='Rural'),
    path('Tweet', views.Tweet.as_view(), name='Tweet'),
    path('Web_Design', views.Web_Design.as_view(), name='Web_Design'),
    path('regis_form', views.regis_form.as_view(), name='regis_form'),
    ]
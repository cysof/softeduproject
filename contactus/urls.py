from django.urls import path
from .import views

app_name = "contactus"



urlpatterns = [
    path('', views.home),
    path('hire', views.hirewriter, name="hirewriter"),
    path('contactform/', views.contactuspage, name='contactform'),
]

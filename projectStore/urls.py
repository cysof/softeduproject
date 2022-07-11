from django.urls import path
from .import views 
from .views import ProjectDetail, Department


app_name ="projectStore"


urlpatterns = [
    path('', views.home, name='home'),
    
    path('projectList/', views.projectList, name="projectList"),

    path('hirewriter/', views.hirewriterform, name='hirewriter'),
    
    path('<slug:slug>/', ProjectDetail.as_view(), name='projectDetail'),
    
    path('department', views.department, name="department"),
    
    path('department/<str:depts>/', views.category, name='courses'),
    path('payment', views.payment, name='payment'),
    path('about', views.about, name='about'),
    
]


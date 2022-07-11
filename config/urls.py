from django.contrib import admin
from django.urls import path, include



urlpatterns = [
      path('admin/', admin.site.urls),
      
      path('', include('projectStore.urls')),
      
      path('contactus/', include('contactus.urls')),
      
      
     
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='events'),
    path('<int:event_id>', views.event, name='event'),
   

    
]
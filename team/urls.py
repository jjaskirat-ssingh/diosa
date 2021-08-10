from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='team'),
    path('<int:member_id>', views.member, name='member'),    
]
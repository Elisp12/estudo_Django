from django.urls import path
from . import views



urlpatterns = [
    path('', views.home), # home
    path('part/<int:id>/', views.parts), # part
   
]

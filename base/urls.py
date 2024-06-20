from django.urls import path
from . import views



urlpatterns = [
    path('', views.home), # home
    path('parts/<int:id>/', views.parts), # home
   
]

from django.urls import path
from . import views

app_name = 'parts'

urlpatterns = [
    path('', views.home, name='home'), # home
    path('part/<int:id>/', views.parts, name='part'), # part
   
]

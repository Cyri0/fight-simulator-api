from django.urls import path
from . import views

urlpatterns = [
    path('fighters/', views.getFighters),
    path('races/', views.getRaces),
    path('weapons/', views.getWeapons),
    path('weapon/<int:pk>', views.getWeapon),
    path('race/<int:pk>', views.getRace),
]
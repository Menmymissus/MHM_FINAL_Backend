from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_stress_level,name='predict_stress_level' ),
]
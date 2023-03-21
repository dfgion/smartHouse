from django.urls import path
from .views import CreateSensorView, UpdateView, CreateMeasurementView, InfoAbOneView

urlpatterns = [
    path('sensors/', CreateSensorView.as_view()),
    path('sensors/<pk>/', UpdateView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
    path('sensors/<pk>/', InfoAbOneView.as_view())
    
]

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, OneSensorSerializer
from pprint import pprint
import ast
    
class CreateSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
        
class UpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    def patch(self, request, *args, **kwargs):
        self.serializer_class = SensorSerializer 
        return super().patch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        self.serializer_class = OneSensorSerializer
        return super().get(request, *args, **kwargs)
    
class CreateMeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        data = ast.literal_eval(request.body.decode('utf-8')) # преобразование битовой строки в словарь
        try:
            Measurement(sensor_id=data['sensor_id'], temperature=data['temperature']).save()
            return Response({'status': 'OK'})
        except Exception as ex:
            return Response({'status': 'Error'})

class InfoAbOneView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = OneSensorSerializer


        

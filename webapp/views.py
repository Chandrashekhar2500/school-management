from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import teachers
from . models import students
from . serializers import teacherSerializer
from . serializers import studentSerializer


class teacherList(APIView):

    def get(self, request):
        teachers1 = teachers.objects.all()
        serializer = teacherSerializer(teachers1, many = True)
        return Response(serializer.data)
    
    
    def post(self):
        pass    

class studentList(APIView):

    def get(self, request):
        students1 = students.objects.all()
        serializer = studentSerializer(students1, many = True)
        return Response(serializer.data)
    
    
    def post(self):
        pass

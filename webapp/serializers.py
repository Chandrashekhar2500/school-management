from rest_framework import serializers
from .models import teachers
from .models import students

class teacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = teachers
        fields = '__all__'   

class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model = students
        fields = '__all__'
from rest_framework import serializers
from .models import Cse23_27

class Cse23_27Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cse23_27
        fields = '__all__'  # Include all fields

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cse23_27
from .serializers import Cse23_27Serializer

@api_view(['GET'])
def get_all_students(request):
    students = Cse23_27.objects.all()  # Fetch all records
    serializer = Cse23_27Serializer(students, many=True)
    return Response(serializer.data)  # Return JSON response

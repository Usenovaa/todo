from rest_framework.decorators import api_view
from .models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer


@api_view(['GET'])
def task_list(request):
    queryset = Task.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    return Response(serializer.data, status=200)



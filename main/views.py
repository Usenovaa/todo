from rest_framework.decorators import api_view
from .models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer


@api_view(['GET'])
def task_list(request):
    queryset = Task.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['PUT', 'PATCH'])
def task_update(request, pk):
    try:
        task = Task.objects.get(id=pk)
        if request.method == 'PUT':
            serializer = TaskSerializer(instance=task, data=request.data)

        else:
            serializer = TaskSerializer(instance=task, data=request.data, partial=True)


        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    except Task.DoesNotExist:
        return Response('Такого таска нет', status=404)


@api_view(['DELETE'])
def task_delete(request, pk):
    try: 
        task = Task.objects.get(id=pk)
        task.delete()
        return Response('Deleted Successfully', status=204)
    except Task.DoesNotExist:
        return Response('Task not found', status=404)
    

@api_view(['GET'])
def get_task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response('Task not found')
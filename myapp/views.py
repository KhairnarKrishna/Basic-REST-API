from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelCRUDAPIView(APIView):
    def get(self, request, pk=None, format=None):
        # Retrieve a single instance or all instances of MyModel
        if pk is not None:
            instance = MyModel.objects.get(pk=pk)
            serializer = MyModelSerializer(instance)
        else:
            queryset = MyModel.objects.all()
            serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Create a new instance of MyModel using data from the request
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        # Update an existing instance of MyModel
        instance = MyModel.objects.get(pk=pk)
        serializer = MyModelSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # Delete an existing instance of MyModel
        instance = MyModel.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

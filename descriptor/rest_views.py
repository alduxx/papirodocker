from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Api, Service, ParameterGroup
from .rest_serializers import ApiSerializer

@api_view(['GET', 'POST'])
def api_list(request):
    """
    List all apis or create a new api.
    """
    if request.method == 'GET':
        apis = Api.objects.all()
        serializer = ApiSerializer(apis, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def api_detail(request, api_id):
    """
    Retrieve, update or delete a code api.
    """
    try:
        api = Api.objects.get(pk=api_id)
    except Api.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiSerializer(api)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApiSerializer(api, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ApiSerializer(api, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

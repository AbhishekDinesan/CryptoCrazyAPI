#create all of YOUR ENDPOINTS
from django.http import JsonResponse
from .models import crypto
from .serializers import CryptoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def crypto_list(request):
    if request.method == 'GET':
        c = crypto.objects.all()
        s = CryptoSerializer(c, many = True)
        return Response(s.data)
    
    if request.method == 'POST':
        s = CryptoSerializer(data = request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status= status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def crypto_detail(request, id):
    try: 
        c = crypto.objects.get(pk = id)
    except crypto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        s = CryptoSerializer(c)
        return Response(s.data)
    elif request.method == 'PUT':
        s = CryptoSerializer(c, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        crypto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import UserSerializer

# @api_view(['POST'])
# @csrf_exempt
# def register_user(request):
#     print(request.data)
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         print("serializer is valid")
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
#         response = Response(data, status=status.
#         HTTP_201_CREATED)
#         print("response is", response)
#         response["Access-Control-Allow-Origin"] = "*"
#         response["Access-Control-Allow-Methods"] = "POST"
#         response["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With"
#         return Response(data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.parsers import JSONParser


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = JSONParser().parse(request)
        else:
            data = request.POST
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        response = Response(data, status=status.
        HTTP_201_CREATED)
        print("response is", response)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With"
        return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

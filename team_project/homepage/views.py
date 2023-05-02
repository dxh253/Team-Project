from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework import status


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    email = request.data.get('email')

    if not email:
        return JsonResponse({'error': 'Email is required'}, status=400)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User with this email does not exist'}, status=404)

    # Generate unique reset token
    reset_token = get_random_string(length=32)

    # Set the reset token on the user
    user.reset_token = reset_token
    user.save()

    # Send password reset email
    subject = 'Reset your password'
    # reset_url = f'https://team22-22.bham.team/reset-password/{reset_token}/'
    reset_url = f'http://localhost:8080/reset-password/{reset_token}/'
    message = f'Click this link to reset your password: {reset_url}'
    send_mail(subject, message, 'noreply@example.com',
              [email], fail_silently=False)

    return JsonResponse({'message': 'Password reset email sent'}, status=200)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request, reset_token):
    print(f'The reset token is {reset_token}')
    try:
        user = User.objects.get(reset_token=reset_token)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Invalid reset token'}, status=404)

    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')

    if not password:
        return JsonResponse({'error': 'Password is required'}, status=400)

    if password != confirm_password:
        return JsonResponse({'error': 'Passwords do not match'}, status=400)

    # Set the new password on the user and clear the reset token
    user.password = make_password(password)
    user.reset_token = None
    user.save()

    return JsonResponse({'message': 'Password reset successful'}, status=200)

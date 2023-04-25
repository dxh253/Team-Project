from django.core.signing import BadSignature, SignatureExpired, loads
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt


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


@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    if user:
        token = jwt.encode({'user_id': user.id},
                        'secret_key', algorithm='HS256')
        link = request.build_absolute_uri(f'/reset-password/{token.decode("utf-8")}/')
        message = f'Click the link below to reset your password:\n\n{link}'
        send_mail('Password reset for your account', message, 'from@example.com', [email])
    return Response({'message': 'If the provided email exists in our database, an email with instructions to reset your password will be sent.'})

@csrf_exempt
@api_view(['POST'])
def reset_password(request, token):
    print(f'Token: {token}')
    UserModel = get_user_model()

    # Verify the token's validity
    try:
        user_id = loads(token, max_age=86400)  # 1 day
    except SignatureExpired:
        return render(request, 'reset_password_expired.html')
    except BadSignature:
        return render(request, 'reset_password_invalid.html')

    # Get the user object from the database
    try:
        user = UserModel.objects.get(pk=user_id)
    except UserModel.DoesNotExist:
        return render(request, 'reset_password_invalid.html')

    # Render the password reset form
    if request.method == 'POST':
        password = request.POST.get('password')
        user.set_password(password)
        user.save()
        return redirect('/login/')
    else:
        return render(request, 'reset_password.html')

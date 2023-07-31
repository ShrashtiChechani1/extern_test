from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from exam.models import UserProfile
from django.contrib.auth.hashers import make_password
import re

@api_view(['POST'])
def signup(request):
    try:
        data = request.data
        user_role_name = data.get('user_role')
        email = data.get('email')
        phone_number = data.get('phone_number')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if not user_role_name or not email or not password or not confirm_password or not phone_number:
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if UserProfile.objects.filter(email=email).exists():
            return Response({"message": "Email already exists"}, status=status.HTTP_409_CONFLICT)

        if password != confirm_password:
            return Response({"message": "Password and Confirm Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)

        if len(password) < 8:
            return Response({"message": "Invalid Password. Minimum length 8 characters."}, status=status.HTTP_400_BAD_REQUEST)

        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{8,}$'
        if not re.match(password_regex, password):
            return Response({
                'error': 'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character (@, $, !, %, *, ?, or &).'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Create the User instance
        user = User.objects.create(username=email,email=email)
        user.set_password(password)
        user.save()

        # Create the UserProfile instance with the selected user_role as a string
        user_profile = UserProfile.objects.create(user_role=user_role_name, email=email, phone_number=phone_number, password=make_password(password))
        user_profile.save()

        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

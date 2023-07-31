from rest_framework import status
from rest_framework.response import Response
from functools import wraps

def check_active_user(data):
    @wraps(data)
    def decorator(func):
        if func.user.active_status:            
            return data(func)
        else:
            return Response({"detail":"Authentication credentials were not provided."},status=status.HTTP_401_UNAUTHORIZED)
    return decorator
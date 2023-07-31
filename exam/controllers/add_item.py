from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from exam.models import Item
# from .permissions import CanAddItem

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
# @permission_classes([CanAddItem])
def add_item(request):
    try:
        data = request.data
        name = data.get('name')
        description = data.get('description')

        if not name or not description:
            return Response({'error': 'Name and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Only users with Role2 or Role3 will be allowed to add items
        item = Item.objects.create(name=name, description=description)
        return Response({"message": "Item added successfully."}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

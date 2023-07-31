from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from exam.models import Item

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_items(request):
    items = Item.objects.all()
    serialized_items = []
    for item in items:
        serialized_items.append({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'image_url': item.image.url if item.image else None,
        })

    return Response({"items": serialized_items})

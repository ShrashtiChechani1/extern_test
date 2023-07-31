from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from exam.models import Item

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_item(request):
    if request.user.role not in ['Role2', 'Role3']:
        return Response({"error": "You don't have permission to add items."}, status=403)

    name = request.data.get('name')
    description = request.data.get('description')

    if not name or not description:
        return Response({"error": "Missing 'name' or 'description' parameter."}, status=400)

    # Create the new item
    new_item = Item.objects.create(name=name, description=description)

    return Response({"message": "Item added successfully.", "item_id": new_item.id})

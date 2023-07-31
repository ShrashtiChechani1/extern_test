from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from exam.models import Item

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_item(request):
    # if request.user.role != 'Role3':
    #     return Response({"error": "You don't have permission to delete items."}, status=403)

    item_id = request.data.get('item_id')

    if not item_id:
        return Response({"error": "Missing 'item_id' parameter."}, status=400)

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return Response({"error": "Item not found."}, status=404)

    # Delete the item
    item.delete()

    return Response({"message": "Item deleted successfully."})

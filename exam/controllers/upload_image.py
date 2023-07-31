from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from exam.models import Item

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_image(request):
    item_id = request.data.get('item_id')
    image = request.FILES.get('image')

    if not item_id:
        return Response({"error": "Missing 'item_id' parameter."}, status=400)

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return Response({"error": "Item not found."}, status=404)

    if not image:
        return Response({"error": "No image file provided."}, status=400)

    # Update the image field of the item with the uploaded image
    item.image = image
    item.save()

    return Response({"message": "Image uploaded successfully."})

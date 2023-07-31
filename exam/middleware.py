# # permissions_middleware.py
# from rest_framework.response import Response
# from jwt import decode, ExpiredSignatureError

# class CheckPermissionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         # Get the token from the request headers (assuming it's provided as an authorization header)
#         authorization_header = request.META.get('HTTP_AUTHORIZATION')
#         if not authorization_header or not authorization_header.startswith('Bearer '):
#             return Response('message - Invalid or missing token.')

#         token = authorization_header.split(' ')[1]

#         # Decode the token and extract the user's roles
#         try:
#             decoded_token = decode(token, 'your_secret_key', algorithms=['HS256'])
#             user_roles = decoded_token.get('roles', [])
#         except ExpiredSignatureError:
#             return Response('message - Token has expired.')
#         except Exception:
#             return Response('message - Invalid token.')

#         # List of view function names that do not require permission check
#         views_without_permission_check = ['signup', 'signin']

#         # Check if the current view is in the views_without_permission_check list
#         if view_func.__name__ in views_without_permission_check:
#             return None

#         # Map the view function names to the required permissions
#         permissions_map = {
#             'upload_image': ['Role1'],
#             'add_item': ['Role2', 'Role3'],
#             'delete_item': ['Role3'],
#             'view_items': ['Role1', 'Role2', 'Role3'],
#         }

#         # Get the required permission for the current view function
#         required_permission = permissions_map.get(view_func.__name__)

#         # Check if the user has the required permission
#         if required_permission and not any(role in user_roles for role in required_permission):
#             return Response('message - You do not have the required permission.')

#         return None

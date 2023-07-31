# from django.http import HttpResponseForbidden
# from exam.models import UserProfile

# class ItemPermissionsMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             try:
#                 user_profile = UserProfile.objects.get(email=request.user.email)
#                 user_role = user_profile.user_role
#             except UserProfile.DoesNotExist:
#                 return HttpResponseForbidden("User profile not found.")
            
#             allowed_roles = {
#                 '/api/upload_image/': ['Role1'],
#                 '/api/add_item/': ['Role2', 'Role3'],
#                 '/api/delete_item/': ['Role3'],
#                 '/api/list_items/': ['Role1', 'Role2', 'Role3'],
#             }
#             path = request.path_info
#             if path in allowed_roles and user_role not in allowed_roles[path]:
#                 return HttpResponseForbidden("You don't have permission to access this resource.")
#         response = self.get_response(request)
#         return response

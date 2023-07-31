from exam import views
from django.urls import path,include
from exam.controllers.signup import signup
from exam.controllers.signin import signin
from exam.controllers.add_item import add_item
from exam.controllers.upload_image import upload_image
from exam.controllers.delete_item import delete_item
from exam.controllers.list_items import list_items
urlpatterns = [
    path('',views.index , name = "index"),
    path('signup',signup,name="signup"),
    path('signin',signin,name="signin"),
    path('add_item/', add_item, name='add_item'),
    path('upload_image/',upload_image, name='upload_image'),
    path('delete_item',delete_item,name="delete_item"),
    path('list_items/', list_items, name='list_items'),
]

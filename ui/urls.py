from django.urls import path
from .views import home, create, manage, add, remove

urlpatterns = [
    path('', home, name="home"),
    path('create', create, name="create"),
    path('manage', manage, name="manage"),
    path('add', add, name="add"),
    path('remove', remove, name="remove"),
]
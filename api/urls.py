from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    TasksAPIView,
    TaskAPIView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="To Do List Rest API",
        default_version="v1.0",
        description="To Do List Rest API",
    ),
    public=True,
)

urlpatterns = [
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # ALL
    path("<user_uuid>/tasks", TasksAPIView.as_view(), name="tasks"),
    # By ID
    path("<user_uuid>/task/<task_id>", TaskAPIView.as_view(), name="task"),
]

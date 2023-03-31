from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Task
from .serializers import TaskSerializer

from ui.models import User


class TasksAPIView(APIView):
    @swagger_auto_schema(tags=["Tasks"], responses={200: TaskSerializer(many=True)})
    def get(self, request, user_uuid, format=None):
        user = User.objects.filter(user_uuid=user_uuid)

        if user.exists():
            tasks = user.first().task_set.all()
            tasks_serializer = TaskSerializer(tasks, many=True)
            return Response(tasks_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "User not found !"},
                status=status.HTTP_404_NOT_FOUND,
            )

    @swagger_auto_schema(tags=["Tasks"], request_body=TaskSerializer)
    def post(self, request, user_uuid, format=None):
        user = User.objects.filter(user_uuid=user_uuid)

        if user.exists():
            task = Task(
                user=user.first(),
                title=request.data["title"],
                status=request.data["status"],
            )
            task.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "User not found !"},
                status=status.HTTP_404_NOT_FOUND,
            )


# By ID


class TaskAPIView(APIView):
    @swagger_auto_schema(tags=["Task"], responses={200: TaskSerializer(many=False)})
    def get(self, request, user_uuid, task_id, format=None):
        user = User.objects.filter(user_uuid=user_uuid)

        if user.exists():
            task = user.first().task_set.filter(pk=task_id)
            if task.exists():
                task_serializer = TaskSerializer(task.first(), many=False)
                return Response(task_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "Task not found !"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "User not found !"},
                status=status.HTTP_404_NOT_FOUND,
            )

    @swagger_auto_schema(tags=["Task"], request_body=TaskSerializer)
    def put(self, request, user_uuid, task_id, format=None):
        user = User.objects.filter(user_uuid=user_uuid)

        if user.exists():
            task = user.first().task_set.filter(pk=task_id)
            if task.exists():
                task.update(
                    title=request.data["title"],
                    status=request.data["status"],
                )
                return Response(status=status.HTTP_204_NO_CONTENT)

            else:
                return Response(
                    {"message": "Task not found !"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "User not found !"},
                status=status.HTTP_404_NOT_FOUND,
            )

    @swagger_auto_schema(
        tags=["Task"],
    )
    def delete(self, request, user_uuid, task_id, format=None):
        user = User.objects.filter(user_uuid=user_uuid)

        if user.exists():
            task = user.first().task_set.filter(pk=task_id)
            if task.exists():
                task.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            else:
                return Response(
                    {"message": "Task not found !"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "User not found !"},
                status=status.HTTP_404_NOT_FOUND,
            )

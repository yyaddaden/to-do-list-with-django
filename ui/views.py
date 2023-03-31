from django.shortcuts import render, redirect
from uuid import uuid4

from .models import User


def home(request):
    return render(request, "ui/home.html")


def create(request):
    if request.method == "GET":
        return render(request, "ui/create.html")

    elif request.method == "POST":
        user_name = request.POST.get("user_name")
        user_uuid = uuid4()

        user = User(user_name=user_name, user_uuid=user_uuid)
        user.save()

        return render(
            request, "ui/create.html", {"user_uuid": user_uuid, "user_name": user_name}
        )


def manage(request):
    users = User.objects.all()

    return render(
        request,
        "ui/manage.html",
        {
            "users": users,
        },
    )


def add(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_uuid = uuid4()

        user = User(user_name=user_name, user_uuid=user_uuid)
        user.save()

        return redirect(manage)


def remove(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")

        user = User.objects.get(pk=user_id)
        user.delete()

        return redirect(manage)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.forms import UserLoginForm


def index(request):
    return render(request, "chat/index.html", {'form': UserLoginForm})


@login_required
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

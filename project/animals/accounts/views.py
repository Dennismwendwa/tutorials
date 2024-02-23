from django.shortcuts import render
from .models import Item  # add this import


def index(request):
    items = Item.objects.all()

    context = {
        "items": items
        }
    return render(request, "accounts/index.html", context)

from django.shortcuts import render
from .models import Images


# Create your views here.
def index(request):
    context = {
        "pictures":Images.objects.all()
    }

    return render(request, 'gallery/index.html',context)
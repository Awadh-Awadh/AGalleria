from django.shortcuts import render
from .models import Images
from .forms import PictureForm


# Create your views here.
def index(request):
    context = {
        "pictures":Images.objects.all()
    }

    return render(request, 'gallery/index.html',context)

def upload(request):
    form = PictureForm()
    context = {
        'form':form
    }
    return render(request, 'gallery/load.html',context)
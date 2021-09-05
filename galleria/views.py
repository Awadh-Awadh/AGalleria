from django.shortcuts import render, redirect
from .models import Images
from .forms import PictureForm


# Create your views here.
def index(request):
    context = {
        "pictures":Images.objects.all()
    }

    return render(request, 'gallery/index.html',context)

def upload(request):
    if request.method == 'POST':
        form = form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = PictureForm()
        context = {
            'form':form
        }
    return render(request, 'gallery/load.html',context)
from django.shortcuts import render, redirect
from .models import Images, Cat
from .forms import PictureForm


# Create your views here.
def index(request,):
    query = request.GET.get('q')
    if query:
      search = Images.objects.filter(name__icontains = query)
      return redirect('index',{"search":search})
    else:
        print("mathafaka")


    category = request.GET.get('category')
    if category is None:
        pictures =Images.objects.all()
    else:
        pictures = Images.objects.filter(categs__name = category)

    context = {
        "pictures":pictures,
        "categories":Cat.objects.all()
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



def details(request, pk):
    eachimage = Images.objects.get(id=pk)
    context = {
        'eachimage':eachimage
    }

    return render(request,'gallery/datails.html',context)




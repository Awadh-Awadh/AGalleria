from django.shortcuts import render, redirect
from .models import Images, Cat
from .forms import PictureForm
from django.db.models import Q


# Create your views here.



'''
Main route that displays every image
create a category variable that checks the request passed in the url
if it is a GET request, and the category contains any value, filter images based on that category value
if category is none filter all images

'''
def index(request,):
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


'''
A function that renders the upload route
checks the form method first, if post, create the form instance with request.post and requst.file
args which are values in the form
Then if form is valid and everything filled up , save the data to the db and redirect user to another route

If method is GET, create an instance of a form without any args to provide an empty form for users to redo by rendering the same
route

'''
def upload(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = PictureForm()
        context = {
            'form':form
        }
    return render(request, 'gallery/load.html',context)

'''
A function that takes an id as an arg
Returns each image associated with the passed id


'''

def details(request, pk):
    eachimage = Images.objects.get(id=pk)
    context = {
        'eachimage':eachimage
    }

    return render(request,'gallery/datails.html',context)


'''
create a query variable that stores the value passed in the form as a request to the server
if a value was passed, filter the model with whatever model attribute that matches the query using __icontains
for attributes containing a relationship, get the attribute name first eg for category(categ__name) then match with the query
categ__name__icontains
'''
def search(request):
    query = request.GET.get('q')
    if query:
      searches = Images.objects.filter (name__icontains = query)
      return render(request,'gallery/search.html',{"searches":searches})
    else:
        redirect('index')


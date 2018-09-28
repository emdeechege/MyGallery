from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import *
# Create your views here.
def home(request):
    images = Image.objects.all()
    location = Location.objects.all()
    category = categories.objects.all()

    if 'location' in request.GET and request.GET['location']:
        name = request.GET.get('location')
        images = Image.view_location(name)
        return render(request, 'all-images.html', {"name":name,"images":images })

    return render(request,"all-images.html",{"images":images,"location":location})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

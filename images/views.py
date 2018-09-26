from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'all-images.html')

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/image.html", {"image":image})

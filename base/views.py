from django.shortcuts import render
from utils.parts.factory import make_parts
from .models import Parts


# Create your views here.

def home (request):
    return render(request,'base-home/pages/home.html', context= {
        'parts': Parts.objects.all(),
}) 

def parts (request, id):
    return render(request,'base-home/pages/list_view.html', context= {
        'part': make_parts(),
        'is_detail_page' : True,
})  
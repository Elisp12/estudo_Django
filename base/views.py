from django.shortcuts import render
from utils.parts.factory import make_parts

# Create your views here.

def home (request):
    return render(request,'base-home/pages/home.html', context= {
        'parts': [make_parts() for _ in range(10)],
}) 

def parts (request, id):
    return render(request,'base-home/pages/list_view.html', context={
        'part': [make_parts],
})
from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request,'base-home/pages/home.html', context=
        {'name':'Eliseu',
}) 

def pice (request, id):
    return render(request,'base-home/pages/list_view.html', context=
        {'name':'Eliseu',
})
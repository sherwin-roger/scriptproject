from django.shortcuts import render

# Create your views here.

def volumeofcylinder(request):
    context = {}
    r=int(request.GET.get('value_a',0))
    h=int(request.GET.get('value_b',0))
    context["value1"]=r
    context["value2"]=h
    return render(request,'mathapp/volumeofcylinder.html', context)

def areaoftriangle(request):
    context = {}
    b=int(request.GET.get('value_a',0))
    h=int(request.GET.get('value_b',0))
    context["value1"]=b
    context["value2"]=h
    return render(request,'mathapp/areaoftriangle.html', context)
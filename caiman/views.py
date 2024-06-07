from django.shortcuts import render

# Create your views here.
def agregarproducto(request):
    return render(request,'caiman/agregarproducto.html')
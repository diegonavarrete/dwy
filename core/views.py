from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def registro(request):
    return render(request, 'core/registro.html')
    
def registroInsumo(request):
    return render(request, 'core/registroInsumo.html')
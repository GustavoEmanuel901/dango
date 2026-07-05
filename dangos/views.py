from django.shortcuts import render
from . import views
# Create your views here.

def index(request):
    """Página principal do aplicativo Dango."""
    return render(request, 'dangos/index.html')
from django.shortcuts import render
from . import views
from .models import Topic, Entry
# Create your views here.

def index(request):
    """Página principal do aplicativo Dango."""
    return render(request, 'dangos/index.html')

def topics(request):
    """Exibe todos os tópicos."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'dangos/topics.html', context)
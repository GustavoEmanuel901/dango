from django.shortcuts import redirect, render
from django.urls import reverse
from . import views
from .models import Topic, Entry
from .forms import TopicForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    """Página principal do aplicativo Dango."""
    return render(request, 'dangos/index.html')

def topics(request):
    """Exibe todos os tópicos."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'dangos/topics.html', context)

def topic(request, topic_id):
    """Exibe um único tópico e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'dangos/topic.html', context)

def new_topic(request):
    """Adiciona um novo tópico."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco.
        form = TopicForm()
    else:
        # Dados submetidos; processa os dados.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))

    # Exibe um formulário em branco ou inválido.
    context = {'form': form}
    return render(request, 'dangos/new_topic.html', context)
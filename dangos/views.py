from django.shortcuts import redirect, render
from django.urls import reverse
from . import views
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    """Página principal do aplicativo Dango."""
    return render(request, 'dangos/index.html')

@login_required
def topics(request):
    """Exibe todos os tópicos."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'dangos/topics.html', context)

@login_required
def topic(request, topic_id):
    """Exibe um único tópico e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'dangos/topic.html', context)

@login_required
def data_table(request):
    """Exibe uma tabela de exemplo para treinar a ocultação de colunas."""
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'dangos/table.html', context)

@login_required
def new_topic(request):
    """Adiciona um novo tópico."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco.
        form = TopicForm()
    else:
        # Dados submetidos; processa os dados.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))

    # Exibe um formulário em branco ou inválido.
    context = {'form': form}
    return render(request, 'dangos/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Adiciona uma nova entrada para um tópico específico."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco.
        form = EntryForm()
    else:
        # Dados submetidos; processa os dados.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    # Exibe um formulário em branco ou inválido.
    context = {'topic': topic, 'form': form}
    return render(request, 'dangos/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Requisição inicial; preenche o formulário com a entrada atual.
        form = EntryForm(instance=entry)
    else:
        # Dados submetidos; processa os dados.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'dangos/edit_entry.html', context)
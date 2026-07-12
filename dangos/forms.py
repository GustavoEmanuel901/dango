from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do tópico',
            }),
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Digite sua anotação aqui',
            }),
        }

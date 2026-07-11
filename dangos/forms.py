from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta: 
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from .forms import CustomUserCreationForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
    

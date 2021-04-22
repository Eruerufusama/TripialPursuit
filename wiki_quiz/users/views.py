from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from users.forms import UserRegsiterForm

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegsiterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created!')
            return redirect('login')
    else:
        form = UserRegsiterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/profile.html')
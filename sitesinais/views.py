from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CadastroForm


def home(request):
    apear_login = True
    if request.user.is_authenticated:
        return redirect('/my-page/')

    if request.method == "GET":
        return render(request, 'sitesinais/pages/index.html',
                      {'apear_login': apear_login})
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect('/my-page/')
        else:
            return redirect('/')


def cadastro(request):
    apear_register = True
    form = CadastroForm()
    if request.user.is_authenticated:
        return redirect('/my-page/')

    if request.method == "GET":
        return render(request, 'sitesinais/pages/cadastro.html',
                      {'form': form,
                       'apear_register': apear_register})
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/confirmacao/')

        else:
            return render(request, 'sitesinais/pages/cadastro.html',
                          {'form': form,
                           'apear_register': apear_register})


@login_required(login_url='/')
def trial(request):
    apear_button = True
    return render(request, 'sitesinais/pages/trial.html',
                  {'apear_button': apear_button})


def confirmacao(request):
    if request.user.is_authenticated:
        return redirect('/my-page/')
    apear_register = True
    return render(request, 'sitesinais/pages/confirmacao.html',
                  {'apear_register': apear_register})


def logout_view(request):
    logout(request)
    return redirect('/')

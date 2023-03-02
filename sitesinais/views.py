import random

import pusher
from decouple import config
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .forms import CadastroForm
from .models import CustomUser, Dados, Sinais


def home(request):
    apear_login = True
    if request.user.is_authenticated:
        return redirect('/my-page/')

    elif request.method == "GET":
        return render(request, 'sitesinais/pages/index.html',
                      {'apear_login': apear_login})
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user:
            activate = CustomUser.objects.get(email=email)
            activate = activate.is_trusty
            if activate is not False:
                login(request, user)
                return redirect('/my-page/')
            else:
                request.session['confirm_email'] = email
                return redirect('/confirmacao/')
        else:
            messages.error(request, 'Email e/ou Senha inválidos')
            return render(request, 'sitesinais/pages/index.html',
                          {'apear_login': apear_login})


def cadastro(request):
    apear_register = True
    form = CadastroForm()
    #  verifica se o usuario ja esta authenticado e tenta acessar a pagina cadastro
    if request.user.is_authenticated:
        return redirect('/my-page/')
    # verifica se o methodo da pagina é GET para renderizar o template
    if request.method == "GET":
        return render(request, 'sitesinais/pages/cadastro.html',
                      {'form': form,
                       'apear_register': apear_register})
    #  se o methodo for POST entra no else
    else:
        form = CadastroForm(request.POST)
        #  verifica se o formulario é valido ao que pede no forms.CustomUser
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.confirmation = random.randint(100000, 999999)
            user.save()
            email = user.email
            confirmation = user.confirmation
            message = f'Código de Ativação: {confirmation}'
            from_email = config('EMAIL_HOST_USER')
            send_mail(subject='Cadastro',
                      message=message,
                      from_email=from_email,
                      recipient_list=[email])
            request.session['confirm_email'] = email

            return redirect('/confirmacao/')
        #  se não for valido renderiza novamente o template porem mostra os erros!
        else:
            return render(request, 'sitesinais/pages/cadastro.html',
                          {'form': form,
                           'apear_register': apear_register, })


def confirmacao(request):
    apear_register = True
    if request.user.is_authenticated:
        return redirect('/my-page/')
    email = request.session.get('confirm_email')
    if request.method == 'GET':
        return render(request, 'sitesinais/pages/confirmacao.html',
                      {'apear_register': apear_register})
    else:
        if email:
            user = CustomUser.objects.get(email=email)
            cod = int(request.POST.get('cod-confirm'))
            if int(user.confirmation) != cod:
                messages.error(request, 'Código incorreto!')
                return render(request, 'sitesinais/pages/confirmacao.html',
                              {'apear_register': apear_register})
            else:
                user.is_trusty = True
                user.save()
                return redirect('/')


@login_required(login_url='/')
def trial(request):
    apear_button = True
    results = Dados.objects.order_by(
        '-id')[:14].values('number', 'date', 'background')
    context = {'results': results}
    return render(request, 'sitesinais/pages/trial.html',
                  context=context,
                  )


def logout_view(request):
    logout(request)
    return redirect('/')


def get_last_results(request):
    results = Dados.objects.order_by(
        '-id')[:14].values('number', 'date', 'background')
    html = render_to_string(
        'sitesinais/partials/dashboard/latest_results.html', {'results': results})
    return HttpResponse(html)


def get_signal(request):
    results = Sinais.objects.order_by(
        '-id')[:1].values('id', 'background', 'date')
    dados = {'dados': list(results)}
    return JsonResponse(dados)

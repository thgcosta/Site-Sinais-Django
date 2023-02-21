from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'sitesinais/pages/index.html')


def cadastro(request):
    apear_register = True

    if request.method == "GET":
        return render(request, 'sitesinais/pages/cadastro.html', 
                      {'apear_register': apear_register})
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')
        referal = request.POST.get('referal')
        senha = request.POST.get('senha')
        user = User.objects.filter(email=email).first

        if user:
            return HttpResponse('Vixi ta ramelando em!')
        
        user = User.objects.create_user()
        return HttpResponse(nome)


def trial(request):
    apear_button = True
    return render(request, 'sitesinais/pages/trial.html',
                  {'apear_button': apear_button})


def confirmacao(request):
    apear_register = True
    return render(request, 'sitesinais/pages/confirmacao.html',
                  {'apear_register': apear_register})
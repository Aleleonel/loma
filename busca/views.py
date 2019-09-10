from django.shortcuts import render, get_object_or_404
from .models import Contato


def page_principal(request):
    contatos = Contato.objects.all()
    return render(request, 'busca/index.html', {'contatos': contatos})


def contatoView(request, id):
    contato = get_object_or_404(Contato, pk=id)
    return render(request, 'busca/contato.html', {'contato': contato})


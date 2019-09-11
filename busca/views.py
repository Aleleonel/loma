from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from .forms import ContatoForm


def page_principal(request):
    contatos = Contato.objects.all().order_by('-created_at')
    return render(request, 'busca/index.html', {'contatos': contatos})


def contatoView(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id)
    return render(request, 'busca/contato.html', {'contato': contato})

def addcontato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():
            contato = form.save(commit=False)
            contato.status = 'Em Atendimento'
            contato.save()
            return redirect('/')
    else:
        form = ContatoForm()
        return render(request, 'busca/addcontato.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def home(request):
  pessoas = Pessoa.objects.all()
  return render(request, 'index.html', {"pessoas": pessoas})

def salvar(request):
  nomeV = request.POST.get('nomeVoluntario')
  Pessoa.objects.create(nomeVoluntario = nomeV)
  pessoas = Pessoa.objects.all()
  return render(request,'index.html',{'pessoas' : pessoas})

def editar(request, id):
  pessoa = Pessoa.objects.get(id=id)
  return render(request, "update.html", {"pessoa" : pessoa})

def update(request,id):
  nomeV = request.POST.get("nomeVoluntario")
  pessoa = Pessoa.objects.get(id=id)
  pessoa.nomeVoluntario = nomeV
  pessoa.save()
  return redirect(home)

def delete(request, id):
  pessoa = Pessoa.objects.get(id=id)
  pessoa.delete()
  return redirect(home)

from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import LivroModel
from .forms import LivroForm

import requests
# Create your views here.

class LivroViewList(ListView):
    model = LivroModel
    template_name = "livros/listar_livros.html"
    context_object_name = "livros"

class LivroCreateView(CreateView):
    model = LivroModel
    form_class = LivroForm
    template_name = "livros/adicionar_livro.html"
    success_url = reverse_lazy("listar_livros")

class LivroUpdateView(UpdateView):
    model = LivroModel
    form_class = LivroForm
    template_name = "livros/atualizar_livro.html"
    success_url = reverse_lazy("listar_livros")
    context_object_name = "livro"

class LivroDeleteView(DeleteView):
    model = LivroModel
    template_name = "livros/deletar_livro.html"
    success_url = reverse_lazy("listar_livros")
    context_object_name = "livro"

class BuscarLivroView(View):
    def get(self, request):
        livros = LivroModel.objects.all()
        return render(request, "livros/buscar_livro.html", {"livros": livros})
    
    def post(self, request):
        livro_id = request.POST.get("livro_id")
        info_livro = None
        
        try:
            livro = LivroModel.objects.get(id=livro_id)
            titulo = livro.titulo
            
            url = f"https://openlibrary.org/search.json?title={titulo}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data["docs"]:
                    doc = data["docs"][0]
                    info_livro = {
                        "titulo": doc.get("title"),
                        "autor": doc.get("author_name", ["Desconhecido"])[0],
                        "ano": doc.get("first_publish_year", "N/A"),
                        "idiomas": doc.get("language", "Linguagem Desconhecida"),
                    }
            else:
                messages.error(request, "Erro ao consultar a API.")

        except LivroModel.DoesNotExist:
            messages.error(request, "Livro não encontrado.")

        livros = LivroModel.objects.all()
        return render(request, "livros/buscar_livro.html", {"livros": livros, "info_livro": info_livro})
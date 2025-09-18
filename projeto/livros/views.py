from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import LivroModel

# Create your views here.

class LivroViewList(ListView):
    model = LivroModel
    template_name = "listar_livros.html"
    content_object_name = "livros"

class LivroCreateView(CreateView):
    model = LivroModel
    form_class = LivroForm
    template_name = "adicionar_livro.html"
    success_url = reverse_lazy("listar_livro")

class LivroUpdateView(UpdateView):
    model = LivroModel
    form_class = LivroForm
    template_name = "atualizar_livro.html"
    success_url = reverse_lazy("listar_livro")

class LivroDeleteView(DeleteView):
    model = LivroModel
    form_class = LivroForm
    template_name = "deletar_livro.html"
    success_url = reverse_lazy("listar_livro")
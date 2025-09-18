from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import LivroModel
from .forms import LivroForm

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

class LivroDeleteView(DeleteView):
    model = LivroModel
    template_name = "livros/deletar_livro.html"
    success_url = reverse_lazy("listar_livros")
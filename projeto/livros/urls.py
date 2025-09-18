from django.urls import path
from .views import(
    LivroViewList,
    LivroCreateView,
    LivroUpdateView,
    LivroDeleteView,
)

urlpattern = [
    path("livros/", LivroViewList.as_view(), name="listar_livro"),
    path("livros/", LivroCreateView.as_view(), name="adicionar_livro"),
    path("livros/", LivroUpdateView.as_view(), name="atualizar_livro"),
    path("livros/", LivroDeleteView.as_view(), name="deletar_livro"),

]
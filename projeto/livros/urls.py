from django.urls import path
from .views import(
    LivroViewList,
    LivroCreateView,
    LivroUpdateView,
    LivroDeleteView,
)

urlpatterns = [
    path("livros/", LivroViewList.as_view(), name="listar_livros"),
    path("livros/adicionar", LivroCreateView.as_view(), name="adicionar_livro"),
    path("livros/<int:pk>/atualizar", LivroUpdateView.as_view(), name="atualizar_livro"),
    path("livros/<int:pk>/deletar", LivroDeleteView.as_view(), name="deletar_livro"),
]
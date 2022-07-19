from rest_framework.viewsets import ModelViewSet

from core.models import Autor, Categoria, Editora, Livro
from core.serializers import AutorSerializer ,CategariaSerializer, EditoraSerializer, LivroDetailSerializer, LivroSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class =CategariaSerializer

class EditorasViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    #serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivroDetailSerializer
        return LivroSerializer


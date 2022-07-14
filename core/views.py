from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora
from core.serializers import CategariaSerializer, EditoraSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class =CategariaSerializer
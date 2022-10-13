from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializers import CategariaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class =CategariaSerializer
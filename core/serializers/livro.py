from rest_framework.serializers import ModelSerializer

from core.models import Autor, Livro

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth =1
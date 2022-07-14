
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.models import Editora

from core.views import CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditorasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls),)
]

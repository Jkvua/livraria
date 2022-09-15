
from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from core.views import AutorViewSet, CategoriaViewSet, EditorasViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditorasViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('', include(router.urls),)
]


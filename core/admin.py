from django.contrib import admin

from core.models import Categoria

admin.site.register(Categoria)

from core.models import Autor

admin.site.register(Autor)

from core.models import Editora

admin.site.register(Editora)



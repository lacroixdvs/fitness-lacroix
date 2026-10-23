from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'rutinas', RutinaViewSet)
router.register(r'planes-lacroix', PlanLacroixViewSet)
router.register(r'metas', MetaLacroixViewSet)
router.register(r'categorias', CategoriaBlogViewSet)
router.register(r'progresos', ProgresoDiarioViewSet)

urlpatterns = router.urls
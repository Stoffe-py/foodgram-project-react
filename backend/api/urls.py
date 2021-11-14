from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import IngredientsViewSet, ReceptViewSet, TagsViewSet

app_name = 'api'

router = DefaultRouter()
router.register('tags', TagsViewSet)
router.register('ingredients', IngredientsViewSet)
router.register('recipes', ReceptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

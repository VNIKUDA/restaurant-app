from django.urls import path, include
from restaurant.api.viewsets import CategoryViewSet, DishViewSet
from restaurant.api.views import CategoryDishes
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"dishes", DishViewSet, basename="dish")

urlpatterns = [
    path('', include(router.urls)),

    # path('category-dishes/<int:id>/', CategoryDishes.as_view(), name="category-dishes"),
]
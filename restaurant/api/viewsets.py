from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from restaurant.models import Category, Dish
from restaurant.api.serializers import CategorySerializer, DishSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=["get"])
    def dish_list(self, request, pk=None):
        category = self.get_object()

        category_dish_list = DishSerializer(category.dishes.all(), many=True)

        return Response(category_dish_list.data)


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
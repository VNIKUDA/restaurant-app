from rest_framework import generics
from restaurant.api.serializers import DishSerializer
from restaurant.models import Category, Dish

class CategoryDishes(generics.ListAPIView):
    serializer_class = DishSerializer
    
    def get_queryset(self):
        return Dish.objects.filter(category_id=self.kwargs.get("id"))
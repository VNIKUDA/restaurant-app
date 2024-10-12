from restaurant.models import Category, Dish
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    dishes = serializers.HyperlinkedIdentityField(view_name="category-dish-list")

    class Meta:
        model = Category
        fields = ["id", "name", "icon", "dishes"]


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ["id", "name", "description", "price"]
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="category_icon/", blank=True)

    def __str__(self):
        return self.name
    

class Dish(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="dishes")
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.price}$"
    

class Picture(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="pictures")
    file = models.ImageField(upload_to="pictures/")

    def __str__(self) -> str:
        return self.dish.name
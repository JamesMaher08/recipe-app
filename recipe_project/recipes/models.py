from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class RecipeBook(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField()

    recipe_yield = models.CharField(max_length=100)
    prep_time = models.CharField(max_length=50)
    total_cook_time = models.CharField(max_length=50)

    cuisine_category = models.CharField(max_length=50)
    meal_type_category = models.CharField(max_length=50)

    recipe_book = models.ForeignKey(RecipeBook, blank=True, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DirectionList(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class IngredientList(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    ingredient_list = models.ForeignKey(IngredientList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Step(models.Model):
    order = models.IntegerField()
    description = models.TextField()
    direction_list = models.ForeignKey(DirectionList, on_delete=models.CASCADE)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.order

class Note(models.Model):
    note = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.note

class Reference(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
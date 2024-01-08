from django.shortcuts import render
from .models import Recipe

recipes = [
    {
        'title': 'Recipe One',
        'author': 'Andrew',
        'date_posted': 'August 28, 2020',
        'last_updated': 'August 28, 2020',
        
        'recipe_yield': '4 people',
        'prep_time': '10 min',
        'total_cook_time': '1 hour',

        'cuisine_category': 'Italian',
        'meal_type_category': 'Dinner'

    }
]

# Create your views here.
def home(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html')

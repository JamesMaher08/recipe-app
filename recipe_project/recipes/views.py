from django.shortcuts import render

recipes = [
    {
        'author': 'Andrew',
        'name': 'Lasanga',
        'ingredient': 'pasta'
    },
    {
        'author': 'James',
        'name': 'Pizza',
        'ingredient': 'pizza'
    }
]

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'recipes': recipes
    }
    return render(request, 'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html')

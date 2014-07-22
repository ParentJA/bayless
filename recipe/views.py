from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.http import require_GET

import json

from recipe.models import Recipe
from recipe.utils import get_request_data


def home(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipe/home.html', {
        'recipes': recipes
    })


@require_GET
def api_recipes(request):
    recipes = [{
        'name': recipe.name,
        'tags': [{
            'type': tag.type,
            'key': tag.key
        } for tag in recipe.tags.all()]
    } for recipe in Recipe.objects.all()]

    try:
        recipes_json = json.dumps(recipes)
    except ValueError:
        return HttpResponseServerError('There was an error converting the recipes and their tags to JSON.')
    else:
        return HttpResponse(recipes_json, content_type='application/json')
import csv

from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe, Ingredient, Favorite, \
    User, Subscription, ShoppingList, RecipeIngredient, Tag


def get_counter(user):
    return Recipe.objects.filter(
        shopping_list__user=user).count


def get_url(tag, tags):
    answer = []
    for i in tags:
        answer.append(i)
    if tag in answer:
        answer.remove(tag)
    else:
        answer.append(tag)
    return "&tag=".join(answer)


def index(request):
    if request.method == 'GET':
        tags = request.GET.getlist('tag')

    available_tags = Tag.objects.all()
    recipes = Recipe.objects.all().filter(tags__name__in=tags)

    counter = 0
    if request.user.is_authenticated:
        counter = get_counter(request.user)

    paginator = Paginator(recipes, 6)
    page_request = request.GET.get('page')
    page = paginator.get_page(page_request)
    tags_and_urls = []
    print(tags)
    for item in available_tags:
        tags_and_urls.append({
            'tag': item,
            'url': get_url(item.name, tags)
        })

    context = {
        'title': 'Рецепты',
        'page': page,
        'paginator': paginator,
        'counter': counter,
        'tags': tags,
        'tags_and_urls': tags_and_urls
    }

    return render(request, 'indexNotAuth.html', context)


def purchases(request):
    user = request.user
    shopping_list = Recipe.objects.filter(shopping_list__user=user)
    counter = get_counter(request.user)
    paginator = Paginator(shopping_list, 6)
    page_request = request.GET.get('page')
    page = paginator.get_page(page_request)
    context = {
        'title': 'Список покупок',
        'shopping_list': shopping_list,
        'page': page,
        'paginator': paginator,
        'counter': counter
    }
    return render(request, 'shopList.html', context)


def login(request):
    context = {
        'title': 'Войти на сайт'
    }
    return render(request, 'authForm.html', context)


def register(request):
    context = {
        'title': 'Регистрация'
    }
    return render(request, 'reg.html', context)


def recipe(request, recipe_id):
    recipe = get_object_or_404(
        Recipe, pk=recipe_id
    )
    context = {
        'title': recipe.title,
        'recipe': recipe

    }
    return render(request, 'singlePage.html', context)


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    counter = get_counter(request.user)
    if form.is_valid():
        my_recipe = form.save(commit=False)
        my_recipe.author = request.user
        my_recipe.save()

        form.save_m2m()
        return redirect(
            'recipe',
            recipe_id=my_recipe.id)

    context = {
        'form': form,
        'title': 'Создать рецепт',
        'counter': counter
    }
    return render(request, 'formRecipe.html', context)


@login_required
def recipe_delete(request, recipe_id):
    return render(request)


@login_required
def recipe_edit(request, recipe_id):
    counter = get_counter(request.user)
    recipe = get_object_or_404(
        Recipe, pk=recipe_id
    )

    form = RecipeForm(request.POST or None,
                      files=request.FILES or None,
                      instance=recipe)

    if request.method == 'POST':
        ing = [v for k, v in request.POST.items()
               if k.startswith('nameIngredient_')]
        if len(ing) == 0:
            return redirect("recipe", recipe_id=recipe_id)

        ingredients = {}
        for item in request.POST:
            if item.startswith('nameIngredient_'):
                num = item[len('nameIngredient_'):]
                ingredients[request.POST[item]] = \
                    int(float(request.POST[f'valueIngredient_{num}']))

        if form.is_valid():
            my_recipe = form.save(commit=False)
            my_recipe.author = request.user
            my_recipe.save()
            my_recipe.recipe_ingredient.all().delete()
            for title, quantity in ingredients.items():
                RecipeIngredient(
                    recipe=recipe,
                    ingredient=Ingredient.objects.filter(name=title)[0],
                    quantity=int(quantity)
                ).save()
            return redirect("recipe", recipe_id=recipe_id)

    context = {
        'title': recipe.title,
        'form': form,
        'recipe': recipe,
        'counter': counter

    }
    return render(request, 'formRecipe.html', context)


def ingredients(request):
    text = request.GET['query']
    ingredients = Ingredient.objects.filter(
        name__icontains=text
    )
    answer = []
    for ingredient in ingredients:
        answer.append({
            'title': ingredient.name,
            'dimension': ingredient.unit,
        })

    return JsonResponse(answer, safe=False)


def favorites(request):
    if request.method == 'GET':
        tags = request.GET.getlist('tag')

    available_tags = Tag.objects.all()
    tags_and_urls = []

    for item in available_tags:
        tags_and_urls.append({
            'tag': item,
            'url': get_url(item.name, tags)
        })

    user = request.user
    counter = get_counter(request.user)
    favorite_recipes = Recipe.objects.filter(
        favorite_recipes__user=user
    ).filter(
        tags__name__in=tags
    )

    paginator = Paginator(favorite_recipes, 6)
    page_request = request.GET.get('page')
    page = paginator.get_page(page_request)
    context = {
        'title': 'Избранное',
        'page': page,
        'paginator': paginator,
        'counter': counter,
        'tags': tags,
        'tags_and_urls': tags_and_urls
    }
    return render(request, 'favorite.html', context)


def favorites_add(request):
    recipe_id = json.loads(request.body).get('id')
    recipe = get_object_or_404(
        Recipe, pk=recipe_id
    )

    _, created = Favorite.objects.get_or_create(
        user=request.user, recipe=recipe
    )

    if not created:
        return JsonResponse({'success': False})

    return JsonResponse({'success': True})


def favorites_remove(request, recipe_id):
    recipe = get_object_or_404(
        Recipe, pk=recipe_id
    )
    removed = Favorite.objects.filter(
        user=request.user, recipe=recipe
    ).delete()

    if removed:
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


def subscriptions(request):
    user = request.user
    counter = get_counter(request.user)
    follower = User.objects.filter(following__user=user)
    paginator = Paginator(follower, 3)
    page_request = request.GET.get('page')
    page = paginator.get_page(page_request)
    recipe: dict = {}
    for sub in follower:
        recipe[sub] = Recipe.objects.filter(
            author=sub
        )[:2]
    context = {
        'title': 'Мои подписки',
        'page': page,
        'paginator': paginator,
        'recipe': recipe,
        'counter': counter

    }
    return render(request, 'myFollow.html', context)


def subscribe_add(request):
    print('add')
    user_id = json.loads(request.body).get('id')
    author = get_object_or_404(User, pk=user_id)
    print(json.loads(request.body))
    _, created = Subscription.objects.get_or_create(
        user=request.user, author=author)

    if not created:
        return JsonResponse({'success': False})

    return JsonResponse({'success': True})


def subscribe_remove(request, user_id):
    author = get_object_or_404(User, pk=user_id)

    removed = Subscription.objects.filter(
        user=request.user, author=author
    ).delete()

    if removed:
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


def purchases_add(request):
    recipe_id = json.loads(request.body).get('id')
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    _, created = ShoppingList.objects.get_or_create(
        user=request.user, recipe=recipe)

    if not created:
        return JsonResponse({'success': False})

    return JsonResponse({'success': True})


def purchases_remove(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    removed = ShoppingList.objects.filter(
        user=request.user, recipe=recipe
    ).delete()

    if removed:
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


def profile(request, username):
    if request.method == 'GET':
        tags = request.GET.getlist('tag')

    available_tags = Tag.objects.all()
    tags_and_urls = []

    profile = get_object_or_404(User, username=username)

    recipes_profile = Recipe.objects.filter(
        author=profile
    ).select_related(
        'author'
    ).filter(tags__name__in=tags
             ).distinct()

    counter = get_counter(request.user)
    paginator = Paginator(recipes_profile, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    for item in available_tags:
        tags_and_urls.append({
            'tag': item,
            'url': get_url(item.name, tags)
        })

    context = {
        'title': 'Рецепты',
        'paginator': paginator,
        'profile': profile,
        'page': page,
        'counter': counter,
        'tags': tags,
        'tags_and_urls': tags_and_urls

    }
    return render(request, 'authorRecipe.html', context)


@login_required
def shoplist(request):
    recipes = Recipe.objects.filter(
        shopping_list__user=request.user
    )

    ing: dict = {}

    for recipe in recipes:
        ingredients = recipe.ingredients.values_list(
            'name', 'unit'
        )
        amount = recipe.recipe_ingredient.values_list(
            'quantity', flat=True
        )

        for num in range(len(ingredients)):
            title: str = ingredients[num][0]
            dimension: str = ingredients[num][1]
            quantity: int = amount[num]

            if title in ing.keys():
                ing[title] = [ing[title][0] + quantity, dimension]
            else:
                ing[title] = [quantity, dimension]

    response = HttpResponse(content_type='txt/csv')
    response['Content-Disposition'] = 'attachment; filename="shop_list.txt"'
    writer = csv.writer(response)

    for key, value in ing.items():
        writer.writerow([f'{key} ({value[1]}) - {value[0]}'])

    return response

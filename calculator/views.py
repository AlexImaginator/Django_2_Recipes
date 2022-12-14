from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def ingridients_list(request, recipe):
    servings = 1
    if request.GET.get('servings'):
        servings = request.GET.get('servings')
    select_recipe = DATA.get(recipe)
    if select_recipe:
        resp = {}
        for ingridient, qty in select_recipe.items():
            resp.update({ingridient: qty*int(servings)})
        context = {'recipe': resp}
    else:
        context = {}
    return render(request, 'calculator/index.html', context)

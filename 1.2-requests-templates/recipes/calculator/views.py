import copy
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
}


def recipes(request, dish):
    servings = int(request.GET.get("servings", 1))
    data_copy = copy.deepcopy(DATA)
    if dish in data_copy.keys():
        context = {'recipe': data_copy[dish]}
    else:
        context = {'recipe': ''}
        return render(request, 'calc.html', context)
    for ingredient in context['recipe'].keys():
        if type(context['recipe'][ingredient]) == float:
            context['recipe'][ingredient] = round(servings * context['recipe'][ingredient], 2)
        else:
            context['recipe'][ingredient] *= servings
    return render(request, 'calc.html', context)

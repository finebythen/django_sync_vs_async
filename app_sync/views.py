import requests, time
from django.http import JsonResponse


def view_sync(request):
    start_time = time.perf_counter()

    pokemons = []
    for num in range(1, 101):
        url = f"https://pokeapi.co/api/v2/pokemon/{num}"
        res = requests.get(url)
        res_json = res.json()
        pokemons.append(res_json['name'])

    amount_pokemons = len(pokemons)
    total_time = time.perf_counter() - start_time

    return JsonResponse({
        'total_time': total_time,
        'amount': amount_pokemons,
        'pokemons': pokemons
    })
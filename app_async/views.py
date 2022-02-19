import aiohttp, asyncio, time
from django.http import JsonResponse


async def get_pokemon(session, url):
    async with session.get(url) as res:
        data = await res.json()
        return data


async def view_async(request):
    start_time = time.perf_counter()

    actions, pokemons = [], []

    async with aiohttp.ClientSession() as session:
        for num in range(1, 101):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            actions.append(asyncio.ensure_future(get_pokemon(session, url)))

        result = await asyncio.gather(*actions)
        for res in result:
            pokemons.append(res['name'])


    count_pokemon = len(pokemons)
    total_time = time.perf_counter() - start_time

    return JsonResponse({
        'total_time': total_time,
        'count': count_pokemon,
        'pokemons': pokemons
    })
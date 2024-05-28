def solution(cacheSize, cities):
    answer = 0

    cache = []
    for city in cities:
        city = city.lower()
        if city not in cache:
            if cacheSize > 0 and len(cache) == cacheSize:
                cache.pop(0)
            if cacheSize > 0:
                cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer
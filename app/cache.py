cache = {}

def get_cache(query):
    return cache.get(query)

def set_cache(query, ans):
    cache[query] = ans


def is_high_rated(movie):
    return movie['imdb'] > 5.5

movie_info = {'name': 'Love', 'imdb': 6.2}
result = is_high_rated(movie_info)

print(result)

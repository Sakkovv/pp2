from func_movies import movies

def score_5_5(movie_name):
    for m in movies:
        if m['name'] == movie_name:
            if m['imdb'] > 5.5:
                return True
    return False

print(score_5_5('Love'))

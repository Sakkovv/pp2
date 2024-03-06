def high_rated_movies(movie_list):
    return [movie for movie in movie_list if movie['imdb'] > 5.5]

num_movies = int(input("Введите количество фильмов: "))
user_movies = []

for i in range(num_movies):
    movie_name = input(f"Введите название фильма {i + 1}: ")
    movie_imdb = float(input(f"Введите рейтинг IMDb для фильма {i + 1}: "))
    user_movies.append({'name': movie_name, 'imdb': movie_imdb})

result = high_rated_movies(user_movies)
print("Фильмы с оценкой IMDb выше 5.5:", result)

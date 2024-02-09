def average_imdb_rating(movie_list):
    if not movie_list:
        return 0.0

    total_rating = sum(movie.get('imdb', 0.0) for movie in movie_list)
    average_rating = total_rating / len(movie_list)
    return average_rating

num_movies = int(input("Введите количество фильмов: "))
user_movies = []

for i in range(num_movies):
    movie_name = input(f"Введите название фильма {i + 1}: ")
    movie_imdb = float(input(f"Введите оценку IMDb для фильма {i + 1}: "))
    user_movies.append({'name': movie_name, 'imdb': movie_imdb})

result = average_imdb_rating(user_movies)
print(f"Средняя оценка IMDb для списка фильмов: {result}")

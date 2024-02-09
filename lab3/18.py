def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie.get('category') == category]

num_movies = int(input("Введите количество фильмов: "))
user_movies = []

for i in range(num_movies):
    movie_name = input(f"Введите название фильма {i + 1}: ")
    movie_category = input(f"Введите категорию для фильма {i + 1}: ")
    user_movies.append({'name': movie_name, 'category': movie_category})

category_input = input("Введите категорию фильмов для поиска: ")
result = movies_by_category(user_movies, category_input)

print(f"Фильмы в категории '{category_input}': {result}")

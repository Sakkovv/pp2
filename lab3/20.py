def category_computes_average(category, movie_list):
    category_movies = movies_by_category(movie_list, category)
    return sum(m['imdb'] for m in category_movies) / len(category_movies) if category_movies else 0.0

movies = []

user_movies = [
    {'name': input(f"Введите название фильма {i + 1}: "),
     'category': input(f"Введите категорию для фильма {i + 1}: "),
     'imdb': float(input(f"Введите оценку IMDb для фильма {i + 1}: "))}
    for i in range(int(input("Введите количество фильмов: ")))
]

category_input = input("Введите категорию для вычисления средней оценки IMDb: ")
result = category_computes_average(category_input, user_movies)

print(f"Средняя оценка IMDb для категории '{category_input}': {result}")

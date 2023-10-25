from collections import defaultdict


def movie_organizer(*args):
    movies = defaultdict(list)
    for movie_name, genre in args:
        movies[genre].append(movie_name)

    result = []
    # sorted by number of movies in genre, then alphabetically
    for movie_genre, films in sorted(movies.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{movie_genre} - {len(films)}")
        [result.append(f"* {movie}") for movie in sorted(films)]

    return "\n".join(result)


# sample inputs
print(movie_organizer(("The Matrix", "Sci-fi")))
print()  # for ease
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print()
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

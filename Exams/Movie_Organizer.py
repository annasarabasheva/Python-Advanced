def movie_organizer(*args):
    dic_movies = {}
    for idx in range(len(args)):
        name = args[idx][0]
        genre = args[idx][1]
        if genre not in sorted(dic_movies):
            dic_movies[genre] = []
        dic_movies[genre].append(name)
    sorted_dict = {key: sorted(value) for key, value in dic_movies.items()}

    dic_movies_sorted = sorted(sorted_dict.items(), key= lambda x: (-len(x[1]), x[0]))
    result = ''
    for idx in range(len(dic_movies_sorted)):
        element = dic_movies_sorted[idx]
        genre = element[0]
        number_movies = len(element[1])
        result += f"{genre} - {number_movies}\n"
        for el in element[1]:
            result += f"* {el}\n"

    return result





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


# Movie Night Planner
# Movie Catalog
movie_catalog = [
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
    {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014},
    {"title": "The Dark Knight", "genre": "Action", "year": 2008},
    {"title": "Titanic", "genre": "Romance", "year": 1997},
    {"title": "Avengers: Endgame", "genre": "Action", "year": 2019}
]

# User Profiles
user_profiles = {
    "Ali": {"watchlist": {"Inception", "Titanic", "Avengers: Endgame"}},
    "Sara": {"watchlist": {"Interstellar", "Titanic", "The Dark Knight"}},
    "Omar": {"watchlist": {"Inception", "The Dark Knight", "Avengers: Endgame"}}
}

# Individual Reports
print("=== Individual Watchlists ===")
for user, data in user_profiles.items():
    print(f"{user}'s Watchlist:")
    for movie in data["watchlist"]:
        print(f" - {movie}")
    print()

# Mutual Picks
mutual_movies = set.intersection(*(data["watchlist"] for data in user_profiles.values()))
print("=== Mutual Picks ===")
print("Movies everyone wants to watch:", ", ".join(mutual_movies), "\n")

# Catalog Match
print("=== Detailed Info for Mutual Picks ===")
for movie in movie_catalog:
    if movie["title"] in mutual_movies:
        print(f"{movie['title']} ({movie['year']}) - Genre: {movie['genre']}")
print()

# Summary & Presentation
total_movies = len(movie_catalog)
unique_movies = set.union(*(data["watchlist"] for data in user_profiles.values()))

print("=== Summary Report ===")
print(f"Total movies in catalog: {total_movies}")
print(f"Unique movies chosen: {len(unique_movies)}")
print(f"Mutual favorites: {len(mutual_movies)}\n")

print("=== Final Group Report ===")
for user in user_profiles:
    print(f"{user} likes {len(user_profiles[user]['watchlist'])} movies.")

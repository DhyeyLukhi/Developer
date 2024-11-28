from imdb import Cinemagoer

ia = Cinemagoer()

movie = input("Movie: ")
items = ia.search_movie(movie)
print("Results: ")
for index, movie in enumerate(items):
    print(f"{index + 1}. {movie['title']} ({movie['year']})")

movie_index = int(input("Movie No.: "))
movie_id = items[movie_index].movieID
info = ia.get_movie(movie_id)

print(f"Title: {info.get('title')}")
print(f"Ratings: {info.get('rating')}")
print(f"Cast: {','.join(info.get('generes', []))}")
print(f"Runtime: {info.get('runtimes', ['N/A'])[0]}")
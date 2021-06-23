from collections import namedtuple


Movie = namedtuple('Movie', ['name', 'genre', 'director'])

avengers = Movie(name='Avengers', genre=['Action', 'Adventure', 'Sci-fi'], director='Joss Whedon')

justice_league = Movie(name='Justice Leagure', genre=['Action', 'Adventure', 'Fantasy'], director='Zack Synder')

def print_movie_info(movie):
    print(f"Name={movie.name} genre={movie.genre} director={movie.director}")

print_movie_info(avengers)
print_movie_info(justice_league)
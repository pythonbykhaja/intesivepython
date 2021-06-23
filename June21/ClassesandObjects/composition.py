class Movie:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self) -> str:
        return self.__name



class Ticket:
    def __init__(self, movie=None, location=None):
        if movie is None:
            movie = Movie('Avengers')

        if location == None:
            location = 'PVR Cinemas'
        
        self.__movie = movie
        self.__location = location

    def __str__(self) -> str:
        return f"movie = {self.__movie}, location = {self.__location}"


    @property
    def movie(self):
        return self.__movie

    @property
    def location(self):
        return self.__location


t1 = Ticket()
print(t1)

m1 = Movie('Justice League')
t2 = Ticket(movie=m1)
print(t2)




class Movie:
    def __init__(self, title):
        self.title = title
    
    def get_title(self):
        return self.title

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move_to(0,0)

    def print(self):
        print(f"({self.x}, {self.y})")


point = Point(3,5)
point.print()
point.reset()
point.print()



        


movie = Movie('Avengers')
print(movie.get_title())
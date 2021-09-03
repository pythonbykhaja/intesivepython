
class Piece:
    def __init__(self, color) -> None:
        self.color = color

    def move(self):
        pass

class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.shape = 'horse'

    def move(self):
        print("Move in L ")


if __name__ == "__main__":
    knight1 = Knight('white')
    knight1.move()
    print(knight1.color)

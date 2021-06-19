class Rating:
    """
    This class represents the Rating
    """
    def __init__(self, rating=0):
        self.rating = rating

    def rate(self, value):
        self.rating = value
    

class Review:
    """
    This represents the Review
    """
    def __init__(self, comment=''):
        self.comment = comment

    def add_comments(self, comment):
        self.comment.append(comment)

    def show(self):
        print(self.comment)



class Movie:
    """
    This class represents the Movie
    """
    def __init__(self, title, ratings=None):
        """
        Initialize the class
        """
        self.title = title
        self.ratings = ratings
        self.reviews = []
    
    def add_review(self, review):
        self.reviews.append(review)

    def show_reviews(self):
        print(f"Title = {self.title} Rating={self.ratings.rating}")
        for review in self.reviews:
            review.show()


rating = Rating(rating=8.4)
avengers = Movie('Avengers The End Game', rating)
review_1 = Review("Amazing, but the more I dwell on it the worse it becomes")
avengers.add_review(review_1)
review_2 = Review("Killed all the other movies, big deception.")
avengers.add_review(review_2)

avengers.show_reviews()



        
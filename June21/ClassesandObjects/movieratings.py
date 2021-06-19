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
        for review in self.reviews:
            review.show()
        
from turtle import mode

from django.db import models
from django.contrib import  auth


# Create your models here.
class Publisher(models.Model):
    """
    This is a company which publishes books
    """
    name = models.CharField(max_length=100,
                            help_text="The name of publisher")
    website = models.URLField(help_text="The publishers website")
    email = models.EmailField(help_text="The publishers email address")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    This represents a book
    """
    title = models.CharField(max_length=100,
                             help_text="The title of the book")
    isbn = models.CharField(max_length=20,
                            verbose_name="ISBN number of the book")
    publication_date = models.DateField(verbose_name="Date the book was published")

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    contributors = models.ManyToManyField('Contributor')


class Contributor(models.Model):
    """
    Contributor to a book, author, co-author, editor
    """
    first_name = models.CharField(max_length=100,
                                  help_text="The contributors first name")
    last_name = models.CharField(max_length=100,
                                 help_text="The contributors last name")
    email = models.EmailField(help_text="Contributors Email id")


class BookContributor(models.Model):
    class ContributorRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role of contributor had in the book",
                            choices=ContributorRole.choices, max_length=20
                            )


class Review(models.Model):
    content = models.TextField(help_text="Review Text")
    ratings = models.IntegerField(help_text="The rating the reviewer has given")
    date_created = models.DateTimeField(auto_now_add=True,
                                        help_text="The datetime the review was created")
    date_edited = models.DateTimeField(auto_now_add=True,
                                       help_text="The datetime the review was last edited")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)

import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .users import User
from .movies import Movie


class ReviewManager(models.Manager):
    def get_by_user_id(self, user):
        return self.filter(user=user)

    def filter_by_movie(self, movie):
        return self.filter(movie=movie)

    def filter_by_rating(self, rating):
        return self.filter(rating=rating)

    def get_by_id(self, review_id):
        return self.filter(id=review_id).first()


class Review(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4, unique=True)
    comment_text = models.TextField(null=False)
    rating = models.FloatField(null=False,default=1.0,validators=[MaxValueValidator(5.0), MinValueValidator(1.0)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, null=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, db_index=True, null=False)

    objects = ReviewManager()

    def serialize(self):
        return {
            'id': self.id,
            'comment_text': self.comment_text,
            'rating': self.rating,
            'user': self.user.serialize(),
        }

    @classmethod
    def create(cls, **kwargs):
        review = Review(
            comment_text=kwargs.get('comment_text'),
            user=kwargs.get('user'),
            movie=kwargs.get('movie'),
            rating=kwargs.get('rating'),
        )

        review.save()
        return review
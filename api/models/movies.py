import uuid
from django.db import models


class MovieManager(models.Manager):
    def get_by_user_id(self, user):
        return self.filter(user=user)

    def get_by_id(self, movie_id):
        return self.filter(id=movie_id).first()

    def filter_by_title(self,title):
        return self.filter(title__icontains=title)


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4, unique=True)
    title = models.TextField(null=False)
    description = models.TextField(null=False)

    objects = MovieManager()

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

    @classmethod
    def create(cls, **kwargs):
        movie = Movie(
            title=kwargs.get('title'),
            description=kwargs.get('description')
        )

        movie.save()
        return movie
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import *

@api_view(['GET'])
def movie_details(request):
    body = json.loads(request.body)

    movie_id = body.get('movie_id')

    if movie_id: 
        movie = Movie.objects.get_by_id(movie_id)

        if movie is not None:
            review_array = Review.objects.filter_by_movie(movie)

            reviews = []

            rating = 0

            for review in review_array:
                rating = rating + review.rating
                reviews.append(review.serialize())

            rating = round(rating/len(review_array),2)

            return Response({**movie.serialize(),'avg_rating': rating,'reviews': reviews},status="200")

        return Response({'message': 'Movie you are trying to review does not exist'},status="400")

    return Response({'message': 'Required fields are missing.'},status="400")
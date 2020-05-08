import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .authentication import authenticate

from api.models import *

@api_view(['POST'])
def create_review(request):
    is_auth, email = authenticate(request)

    if is_auth: 
        body = json.loads(request.body)

        movie_id = body.get('movie_id')
        comment_text = body.get('comment_text')
        rating = body.get('rating')

        if movie_id and comment_text and rating:
            user = User.objects.get_by_email(email)
            movie = Movie.objects.get_by_id(movie_id)

            kwargs = {
                'user': user,
                'movie': movie,
                **body
            }

            if movie is not None:
                if isinstance(rating, float) and rating < 6.0:
                    review = Review.create(**kwargs)

                    return Response({**review.serialize()}, status="200")

                return Response({'message': 'Rating should be less than 5.0 and of type float.'},status="400")

            return Response({'message': 'Movie you are trying to review does not exist'},status="400")

        return Response({'message': 'Required fields are missing.'},status="400")
        
    return Response({'message': 'Not authorized to review the movie'},status="401")
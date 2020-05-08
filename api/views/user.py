import json
import jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import *
from .authentication import authenticate

@api_view(['POST'])
def login(request):
    body = json.loads(request.body)
    email = body.get('email')
    password = body.get('password')

    if email and password:
        if User.objects.get_by_email(email=email) is None:
            return Response({'message': 'Username or Password is not correct'}, status="400")

        user = User.objects.authenticate(email=email, password=password)

        if user is not None:
            payload = {
                'email': user.email,
                'password': user.password,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY").decode('utf-8')}

            response = {
                'user_id': user.id,
                'token': jwt_token.get('token'),
            }

            return Response(response, status="200")

        return Response({'message': 'Username or Password is not correct'}, status="400")

    return Response({'message': 'Required fields are missing'}, status="400")


@api_view(['POST'])
def signup(request):
    body = json.loads(request.body)

    email = body.get('email')
    password = body.get('password')

    if email and password:
        user = User.objects.get_by_email(email=email)
        
        if user is None:
            body.pop('email')
            body.pop('password')
            user = User.objects.create_user(email=email, password=password, **body)
            print(user,'2<><><>')
            payload = {
                'email': user.email,
                'password': user.password,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY").decode('utf-8')}

            response = {
                'user_id': user.id,
                'token': jwt_token.get('token'),
            }

            return Response(response,status="200")

        return Response({'message': 'This email is already registered'}, status="400")

    return Response({'message': 'Required fields are missing'}, status="400")

import json
import uuid

from rest_framework.test import APIRequestFactory
from api.views import *

print('')
print('----------Sign Up test cases-----------')
# Using the standard RequestFactory API to create a form POST request
print('1. All credentials are added')
factory = APIRequestFactory()
request = factory.post('/api/signup',{"first_name": "Stephen","last_name": "Strange", "email": "strange@avengers.com", "password": "strange"}, format='json')
response = signup(request)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)
print('')

print('2. Email credential is missing')
factory = APIRequestFactory()
request = factory.post('/api/signup',{'first_name': 'Stephen','last_name': 'Strange', 'password': 'arrow'}, format='json')
response = signup(request)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)

print('')
print('----------Login test cases-----------')
# Using the standard RequestFactory API to create a form POST request
print('1. All credentials are correct')
factory = APIRequestFactory()
request = factory.post('/api/login',{"email": "strange@avengers.com", "password": "strange"}, format='json')
response = login(request)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)
auth_token = response.data.get('token')

print('2. Password credential is incorrect')
factory = APIRequestFactory()
request = factory.post('/api/login',{"email": "strange@avengers.com", "password": "arrow2"}, format='json')
response = login(request)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)
print('')

print('3. Password credential is missing')
factory = APIRequestFactory()
request = factory.post('/api/login',{"email": "oliver@dc.com"}, format='json')
response = login(request)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)


print('')
print('----------Create Movie test cases-----------')
# Using the standard RequestFactory API to create a form POST request
print('1. All credentials are added')
factory = APIRequestFactory()
request = factory.post('/api/movie/create',{"title": "Captain America: The First Avenger", "description": "During World War II, Steve Rogers decides to volunteer in an experiment that transforms his weak body. He must now battle a secret Nazi organisation headed by Johann Schmidt to defend his nation."}, format='json')
response = create_movie(request)
movie_id = response.data.get('id')
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)
print('')

print('2. Email credential is missing')
factory = APIRequestFactory()
request = factory.post('/api/movie/create',{"title": "Captain America: The First Avenger"}, format='json')
response = create_movie(request)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)

print('')
print('----------Create Review test cases-----------')
print('1. All credentials are added')
factory = APIRequestFactory()
request = factory.post('api/review/create',{'movie_id': movie_id, 'comment_text': 'Great movie', 'rating': 4.5}, HTTP_AUTHORIZATION = 'Bearer '+auth_token,format='json')
response = create_review(request)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)
print('')

print('2. Rating is an integer')
factory = APIRequestFactory()
request = factory.post('api/review/create',{'movie_id': movie_id, 'comment_text': 'Great movie', 'rating': 4}, HTTP_AUTHORIZATION = 'Bearer '+auth_token,format='json')
response = create_review(request)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)
print('')

print('3. Rating credential is missing')
factory = APIRequestFactory()
request = factory.post('api/review/create',{'movie_id': movie_id, 'comment_text': 'Great movie'}, HTTP_AUTHORIZATION = 'Bearer '+auth_token,format='json')
response = create_review(request)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)

print('')
print('----------Fetch Movie details test cases-----------')
# Using the standard RequestFactory API to create a form POST request
print('1. All credentials are correct')
factory = APIRequestFactory()
request = factory.get('/api/movie/'+str(movie_id))
response = movie_details(request,movie_id)
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)
auth_token = response.data.get('token')

print('2. Invalid movie id provided')
factory = APIRequestFactory()
request = factory.get('api/movie'+str(uuid.uuid4()))
response = movie_details(request,uuid.uuid4())
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)

print('')
print('----------Search Movie test cases-----------')
print('1. All credentials are added')
factory = APIRequestFactory()
request = factory.get('api/movie/search/Captain')
response = search_movie(request,'Captain')
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)
print('')

print('2. No movie corresponding to the title test case')
factory = APIRequestFactory()
request = factory.get('api/movie/search/Iron')
response = search_movie(request,'Iron')
print('Response:- ','context=',response.rendered_content,'code=',response.status_code)
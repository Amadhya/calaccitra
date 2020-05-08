from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def Check(request):
    if request.method == 'GET':
        response = {
            'message': 'Connection established',
        }

        return Response(response,status=200)
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView  features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, put, push, patch, delete)',
            'Is similar to traditional django view',
            'Gives youthe most control over your application logic',
            'Is mapped manually to url',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
        

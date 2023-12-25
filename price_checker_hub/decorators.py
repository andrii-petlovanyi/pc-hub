import os
from functools import wraps
from django.http import JsonResponse
from dotenv import load_dotenv

load_dotenv()

def validate_api_key(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token_key = auth_header.split(' ')[1]
        else:
            token_key = None

        expected_token = os.getenv('API_KEY')

        if token_key != expected_token:
            return JsonResponse({'message': "Invalid API key"}, status=401)

        return view_func(request, *args, **kwargs)

    return _wrapped_view

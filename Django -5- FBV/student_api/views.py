from rest_framework.response import Response

def home(request):
    return Response(
        {
            "message": "Welcome to the Home Page"
        }
    )
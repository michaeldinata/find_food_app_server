import json 

from django.http import HttpResponse, JsonResponse
# from django.contrib.auth
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_POST
from .models import Users

def index(request):
    return HttpResponse("Hello, world")

@ensure_csrf_cookie
def session_view(request):
    print('isAuth: ' + str(request.user.is_authenticated))
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True})

@ensure_csrf_cookie
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['x-csrftoken'] = get_token(request)
    return response

@require_POST
def login(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    users = Users.objects.get(email = email)

    if check_password(password, users.password):
        data = {"login": True}
        response = JsonResponse(data)
        return response
    else:
        return JsonResponse({"login": False})

def signup(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = make_password(data.get('password'))
    Users.objects.get_or_create

    return HttpResponse("someone is trying to signup")
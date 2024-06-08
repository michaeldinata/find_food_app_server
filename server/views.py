from django.http import HttpResponse, JsonResponse
from .models import Users

def index(request):
    return HttpResponse("Hello, world")

def login(request):
    authHeaderList = request.headers.get('Authorization').split()
    authType = authHeaderList[0]
    email = authHeaderList[1].split(":")[0]
    password = authHeaderList[1].split(":")[1]
    print(email, password)
    users = Users.objects.get(pk = email)
    if password == users.password:
        data = {"login": True}
        return JsonResponse(data)
    print(users.password)
    return HttpResponse("someone trying to login")

def signup(request):
    return HttpResponse("someone is trying to signup")
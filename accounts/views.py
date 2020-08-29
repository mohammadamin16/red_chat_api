import traceback

from django.db.utils import IntegrityError
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse

from accounts.models import User
from back import utility
from back.utility import get_response


def welcome(request):
    return HttpResponse("Welcome!")


def say_hi(request):
    name = utility.get_data(request).get('name')
    return HttpResponse(f'hello {name}')


def signup(request):
    post_data = utility.get_data(request)
    username = post_data.get('username')
    password = post_data.get('password')
    name     = post_data.get('name')

    try:
        user = User.objects.create_user(username, password, name)
        # teacher = User.objects.get(type='T')
        # teacher.students.add(user)
        # user.teacher = teacher
        msg = f'user {username} created successfully!'
        user = utility.user2json(user)
        data = {'user': user}
        response = utility.get_response(msg, True, data)

    except IntegrityError:
        traceback.print_exc()
        msg = "this username is taken. sorry:)"
        response = utility.get_response(msg, success=False)

    except Exception as e:
        traceback.print_exc()
        msg = "Something goes wrong!"
        response = utility.get_response(msg, success=False)

    return JsonResponse(response)


def login(request):
    post_data = utility.get_data(request)
    username = post_data.get('username')
    password = post_data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        user = utility.user2json(user)
        msg = f'welcome {user["name"]}'
        data = {'user': user}
        response = utility.get_response(msg, success=True, data=data)
    else:
        msg = 'username or password is wrong'
        response = utility.get_response(msg, success=False)

    return JsonResponse(response)


def get_teacher(request):
    try:
        teachers = User.objects.filter(type='T').all()
        response = get_response('Here are the teacher!', True, utility.users2json(teachers))
    except:
        traceback.print_exc()
        response = get_response('something went wrong!', True, )

    return JsonResponse(response)


def is_username_valid(request):
    data = utility.get_data(request)
    username = data.get('username')
    users = User.objects.all()
    usernames = []
    for user in users:
        usernames.append(user.username)
    if username in usernames:
        return HttpResponse(f"{username} is not available :(")
    else:
        return HttpResponse(f"{username} is available :)")

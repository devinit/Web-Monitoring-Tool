import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from account.forms import UserLoginForm
from account.usecases import UserLogin, UserLoginFailedError


@require_http_methods(["GET", "POST"])
def user_login_view(request):

    if request.user and request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        loginForm = UserLoginForm(data={
            'username': username,
            'password': password
        })
        if loginForm.is_valid():
            loginUseCase = UserLogin(
                username=loginForm.cleaned_data['username'],
                password=loginForm.cleaned_data['password'])
            try:
                user = loginUseCase.execute()
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    raise UserLoginFailedError('Invalid username and password')
            except UserLoginFailedError as err:
                loginForm.add_error(None, str(err))

        return render(request, template_name='account/login.html', context={ 'form': loginForm })


    return render(request, template_name='account/login.html')


def user_logout_view(request):
    logout(request)

    return redirect('login')

@csrf_exempt
def users_update(request):
    if request.method == "POST":
        #return HttpResponse(json.dumps(request.POST), status=202)
        try:
            user_id = int(request.POST.get('userid', None))
            username = request.POST.get('username', None)
            user = User.objects.get(id=user_id)
            if username:
                user.username = username
                user.save()
                return JsonResponse({"newusername": user.username})
        except  User.DoesNotExist:
            return JsonResponse({"Error": "User doesnot exist"})

    return HttpResponse(status=405)

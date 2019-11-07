from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout

from account.forms import UserLoginForm
from account.usecases import UserLogin, UserLoginFailedError


@require_http_methods(["GET", "POST"])
def user_login_view(request):

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

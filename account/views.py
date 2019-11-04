from django.urls import reverse_lazy
from django.views.generic import FormView

from account.forms import UserLoginForm
from account.usecases import UserLogin, UserLoginFailedError

class UserLoginView(FormView):
    template_name = 'account/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        self._run_use_case(form)
        return super().form_valid(form)

    def _run_use_case(self, form):
        login = UserLogin(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'])

        try:
            login.execute()
        except UserLoginFailedError as err:
            form.add_error(None, str(err))

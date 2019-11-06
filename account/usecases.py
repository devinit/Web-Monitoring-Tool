from django.contrib.auth import authenticate


class UserLoginFailedError(Exception):
    pass


class UserLogin:

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def execute(self):
        return self._authenticate()

    def _authenticate(self):
        user = authenticate(username=self._username, password=self._password)
        if user is not None:
            return user
        else:
            raise UserLoginFailedError('Invalid username or password')

from django.shortcuts import redirect
from django.contrib.auth.views import LoginView as AbstractLoginView
from django.contrib.auth.views import LogoutView as AbstractLogoutView


class LoginView(AbstractLoginView):
    template_name = 'auth/login.html'

class LogoutView(AbstractLogoutView):
    pass

def set_lang(request, lang):
    request.session['lang'] = lang
    return redirect(request.GET.get('next', '/'))

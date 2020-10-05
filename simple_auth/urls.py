from django.urls import path

from .views import LoginView, LogoutView
from .views import set_lang


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('lang/<str:lang>', set_lang, name='set-lang'),
]

from . import views as akun_views
from django.urls import path

urlpatterns = [
    path('', akun_views.login_form),
    # path('sign-in/', akun_views.signIn),
    path('save-account/', akun_views.save_action),
    path('register/', akun_views.registerForm, name='sign_up'),
]
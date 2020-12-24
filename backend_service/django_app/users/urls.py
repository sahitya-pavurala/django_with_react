from django.urls import path, include

from users.views import APILoginView, APILogoutView, APIUpdatePasswordView
urlpatterns = [
    path('login/', APILoginView.as_view(), name='api_login'),
    path('logout/', APILogoutView.as_view(), name='api_logout'),
    path('update_password/', APIUpdatePasswordView.as_view(), name='api_update_password')
]
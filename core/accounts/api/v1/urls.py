from django.urls import path,include
from .views import *


urlpatterns = [
    path('register/',RegisterApiView.as_view(),name='registration'),
    path('token/login/',CustomAuthToken.as_view(),name='token'),
    path('token/logout/',DestroyAuthToken.as_view()),
]
from django.urls import path,include
from .views import *
from rest_framework import routers

app_name = 'api-v1'

router = routers.DefaultRouter()
router.register('post', PostModelViewSetList)
urlpatterns = router.urls



"""
urlpatterns = [
    path("post",ApiPostList.as_view()),
    path("post/<int:pk>",ApiPostDetail.as_view())
]
"""
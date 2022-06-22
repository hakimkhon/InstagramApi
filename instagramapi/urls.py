from django.urls import path
from .views import StoryAPIView, UserAPIView

urlpatterns = [
    path('users', UserAPIView.as_view()),
    path('stories', StoryAPIView.as_view())
]

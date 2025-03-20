from django.urls import path
from .views import HabitListAPIView, HabitCreateAPIView, HabitDeleteAPIView, HabitDetailAPIView, HabitUpdateAPIView, PublicHabitListAPIView

from tracker.apps import TrackerConfig

app_name = TrackerConfig.name


urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habit-list"),
    path("habits/public/", PublicHabitListAPIView.as_view(), name="public-habit-list"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habits/<int:pk>/", HabitDetailAPIView.as_view(), name="habit-detail"),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("habits/<int:pk>/delete/", HabitDeleteAPIView.as_view(), name="habit-delete"),
]
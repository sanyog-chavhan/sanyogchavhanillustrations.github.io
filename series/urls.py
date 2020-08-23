from django.urls import path
from . import views

urlpatterns = [
    path("", views.series_index, name="series_index"),
    path("<int:pk>/", views.series_detail, name="series_detail"),
]


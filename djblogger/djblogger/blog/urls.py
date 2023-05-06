from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("<slug:post>/", views.post_single, name="post_single"),
]

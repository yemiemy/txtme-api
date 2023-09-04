from django.urls import path
from chat import views

urlpatterns = [
    path("messages/", views.MessageAPIView.as_view(), name="")
]

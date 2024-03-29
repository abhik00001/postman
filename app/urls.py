from django.urls import path
from app import views

urlpatterns = [
    path("get", views.home),
    path("postval", views.savethistodo),
    path("singleget/<int:id>", views.singleget),
    # path("post", views.postval),
]
from django.urls import path
from .views import ViolationListCreateView

urlpatterns = [
    path('violations/', ViolationListCreateView.as_view(), name='violations'),
]

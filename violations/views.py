from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Violation
from .serializers import ViolationSerializer

class ViolationListCreateView(generics.ListCreateAPIView):
    queryset = Violation.objects.all()
    serializer_class = ViolationSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            # Permite GET requests sin autenticación
            return [AllowAny()]
        else:
            # Requiere autenticación para POST requests
            return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import viewsets
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save()

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = []   # No auth for testing

    def perform_create(self, serializer):
        user = self.request.user
        # Save without committing to database immediately
        if user.is_authenticated:
            project = serializer.save(created_by=user)
        else:
            project = serializer.save()

        # Save the many-to-many field users
        project.users.set(self.request.data.get('users', []))


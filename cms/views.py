from rest_framework import generics, permissions

from .models import Content
from .serializers import ContentSerializer


class PublicContentView(generics.RetrieveAPIView):
    queryset = Content.objects.filter(status=Content.Status.PUBLISHED)
    serializer_class = ContentSerializer
    lookup_field = "slug"
    permission_classes = [permissions.AllowAny]

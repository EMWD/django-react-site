from rest_framework import viewsets

from .serializers import *
from ..models import BlogCategory, BlogPost


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

    action_to_serializer= {
        'list': '',
        'retrieve': ''
    }


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


    action_to_serializer= {
        'list': BlogPostListRetrieveSerializer,
        'retrieve': BlogPostListRetrieveSerializer
    }
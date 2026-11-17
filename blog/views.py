from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from .models import Post
from .serializers import PostCreateSerializer, PostListSerializer
from rest_framework.views import APIView


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "data": {
                "posts": serializer.data,
                "count": len(serializer.data)
            },
            "timestamp": timezone.localtime(timezone.now())
        })
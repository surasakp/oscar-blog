from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User

from appblog.models import Post, Category
from .serializers import PostSerializer, CategorySerializer, UserLoginSerializer


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False)
    def category_blogs(self, request, *args, **kwargs):
        post_set = Post.objects.filter(category__category__id=kwargs['pk'])
        serializer = self.get_serializer(post_set, many=True)
        return Response(serializer.data)

    def get_authenticators(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            self.authentication_classes.append(TokenAuthentication)

        return [auth() for auth in self.authentication_classes]


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_authenticators(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            self.authentication_classes.append(TokenAuthentication)

        return [auth() for auth in self.authentication_classes]


class UserLoginViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from ..models.author import Author
from ..models.follow import Follow
from ..serializers.author import AuthorSerializer
from ..serializers.follow import FollowSerializer
from news.serializers.news import NewsSerializer
from users.permission import AuthorOwnerOrReadOnly


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AuthorOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['surname', 'name']

    def perform_create(self, serializer: AuthorSerializer):
        return serializer.save(
            email=self.request.user.email,
            user=self.request.user
        )

    @action(
        methods=['GET', ],
        detail=True,
        url_path='news',
    )
    def get_author_news(self, request: HttpRequest, pk: int):
        author = get_object_or_404(Author, author_id=pk)
        news = author.news.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    @action(
        methods=['POST', ],
        detail=True,
        url_path='follow',
    )
    def follow(self, request: HttpRequest, pk: int):
        get_object_or_404(Author, author_id=pk)
        data = {
            'author': pk,
            'follower': self.request.user.user_id,
        }
        serializer = FollowSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(
        methods=['POST', ],
        detail=True,
        url_path='unfollow',
    )
    def unfollow(self, request: HttpRequest, pk: int):
        follow = Follow.objects.filter(
            follower=self.request.user.user_id,
            author=pk
        )
        follow.delete()
        return Response({'detail': 'Success'}, status=204)

    @action(
        methods=['GET', ],
        detail=True,
        url_path='followers',
    )
    def author_follower_list(self, request: HttpRequest, pk: int):
        get_object_or_404(Author, author_id=pk)
        followers = Follow.objects.filter(author=pk)
        serializer = FollowSerializer(followers, many=True)
        return Response(serializer.data)

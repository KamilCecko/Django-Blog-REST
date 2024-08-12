from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .models import Category, Post, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer
from members.permissions import IsSuperUserOrStaff, CustomPermission


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [CustomPermission]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['author'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class PostDetailView(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):
    queryset = Post.objects.all()
    lookup_field = 'pk'
    permission_classes = [CustomPermission]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentSerializer
        return PostSerializer

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        post_data = PostSerializer(post).data
        return Response(
            data={
                'new_comment': request.data,
                'current_post': post_data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUserOrStaff]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    permission_classes = [CustomPermission]


class PostCommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [CustomPermission]

    def get_queryset(self):
        post_pk = self.kwargs['pk']
        return Comment.objects.filter(post_id=post_pk)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        post_data = PostSerializer(Post.objects.get(pk=self.kwargs['pk'])).data
        return Response(
            data={
                'new_comment': request.data,
                'current_post': post_data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer):
        post_pk = self.kwargs['pk']
        serializer.save(post_id=post_pk)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomPermission]
    lookup_field = 'pk'

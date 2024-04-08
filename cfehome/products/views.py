from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin


class ProductListCreateAPIView(
    UserQuerySetMixin,
    generics.ListCreateAPIView,
    StaffEditorPermissionMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content', title)
        serializer.save(user=self.request.user, content=content)

    def get_queryset(self, *args, **kwargs):
        user = self.request.user

        if user.is_anonymous:
            return Product.objects.none()

        if user.is_authenticated:
            queryset = super().get_queryset(*args, **kwargs)
            return queryset.filter(user=user)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(
    UserQuerySetMixin,
    generics.RetrieveAPIView,
    StaffEditorPermissionMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(
    UserQuerySetMixin,
    generics.UpdateAPIView,
    StaffEditorPermissionMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    generics.DestroyAPIView,
    StaffEditorPermissionMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


class ProductListAPIView(
    generics.ListAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListAPIView.as_view()


class ProductMixingView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    lookup_field = 'pk'

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwarg):
        pk = kwarg.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwarg)
        return self.list(request, *args, **kwarg)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


product_mixin_view = ProductMixingView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data

        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content', title)
            serializer.save(content=content)
            return Response(serializer.data)

        return Response({"invalid": "not good data"}, status=400)

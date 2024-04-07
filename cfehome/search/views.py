from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        results = Product.objects.none()
        if query:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = queryset.search(query, user=user)
        return results

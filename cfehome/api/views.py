from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"invalid": "invalid data"}, status=400)

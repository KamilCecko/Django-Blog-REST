import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    ''' DRF API View'''

    # data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # data = serializer.save()
        # print(serializer.data)
        # data = serializer.data

    # instance = Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
    #     data = ProductSerializer(instance).data
        return Response(serializer.data)
    return Response({"invalid" : "not good data"}, status=400)





    # toto je aby si nemusel vsetko pisat osobitne tak pouzijes model to dict
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price


    # print(data)
    # data=dict(data)
    # # json_data_str = json.dumps(data) premiena jason data do stringu
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})
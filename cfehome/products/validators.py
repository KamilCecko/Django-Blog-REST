from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

# def vaidate_title(value):
#     qs = Product.objects.filter(title_iexact=value)
#     # print(value)
#     if qs.exist():
#         raise serializers.ValidationError(f"{value}")
#     return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} is not allowed")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup="iexact")
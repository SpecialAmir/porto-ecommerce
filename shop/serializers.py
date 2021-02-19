
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import Product, Customer, Category, Order


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

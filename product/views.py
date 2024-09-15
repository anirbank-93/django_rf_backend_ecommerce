from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.db.models import Q

# Serializers
from .serializers import (
    CreateProductCategorySerializer,
    CreateProductSerializer,
    ViewProductsSerializer
)

# Models
from .models import Product

#Renderers
from .renderers import ProductDataRenderer

# Create your views here.
class CreateProductCategoryView(APIView):
    renderer_classes = [ProductDataRenderer]

    def post(self, request, format=None):
        serializer = CreateProductCategorySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        return Response(
            {"msg": "Product category created!"},
                status=status.HTTP_201_CREATED,
        )

class CreateProductView(APIView):
    renderer_classes = [ProductDataRenderer]

    def post(self, request, format=None):
        serializer = CreateProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        return Response(
            {"msg": "Product created!"},
                status=status.HTTP_201_CREATED,
        )

class GetProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ViewProductsSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('query', None)

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
        
        return queryset

    def list(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                'msg': "Get products successfully!",
                'data': serializer.data,
            }, status=status.HTTP_200_OK
        )
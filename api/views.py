from rest_framework import generics
from app.models import Category, Product
from .serializers import (
    CategoryListSerializer,
    ProductDetailSerializer,
    CategoryDetailSerializer,
    ProductListSerializer,
)
from rest_framework.response import Response


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category
    serializer = CategoryListSerializer

    def get(self, request):
        return Response({self.serializer(self.queryset.objects.all(), many=True).data})

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class CategoryDetailView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductListSerializer

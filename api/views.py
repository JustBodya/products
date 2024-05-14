from .models import Product, Category
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Product.objects.all()[:5]
        
        return Product.objects.filter(pk=pk)


    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products, UsersProducts
from .serializers import ProductSerializer, UsersProductSerializer


class ProductsView(APIView):
    """

    """
    def get(self, request, product_id: int = None):
        if product_id:
            try:
                product = Products.objects.get(id=product_id)
                serializer = ProductSerializer(product)
            except Products.DoesNotExist:
                return Response("Product does not exist.", status=status.HTTP_404_NOT_FOUND)
        else:
            products = Products.objects.all()
            serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class UsersProductsView(APIView):
    """

    """
    def get(self, request):
        pass

    def post(self, request):
        """

        """
        serialized = UsersProductSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        # if UsersProducts.objects.filter(username=serialized.validated_data['product']).exists():
        #     return Response("Purchase already exists.", status=status.HTTP_400_BAD_REQUEST)

        users_products = UsersProducts.objects.create(**serialized.validated_data)

        return Response({"message": "Successfully transaction"}, status=status.HTTP_201_CREATED)



from .models import Product, Order
from rest_framework import permissions, generics
from .serializers import ProductSerializer, OrderSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrCreate
class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
      """
      This view should return a list of all the purchases
      for the currently authenticated user.
      """
      search = self.request.query_params.get('search')
      if search is not None:
        return Product.objects.filter(title__contains=search).filter(description__contains=search)
      
      return Product.objects.all()

class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrCreate]

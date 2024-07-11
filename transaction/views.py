from .serializers import TransactionSerializer
from .models import Transaction
from rest_framework import viewsets
from rest_framework import permissions
# from rest_framework.authentication import TokenAuthentication

# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

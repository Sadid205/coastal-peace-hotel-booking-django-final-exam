from .serializers import TransactionSerializer
from .models import Transaction
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes
from django.utils import timezone
from django.db.models import Sum
from rest_framework.response import Response
from datetime import timedelta
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TransactionTotals(request):
    now = timezone.now()

    total_amount = Transaction.objects.aggregate(total=Sum('transaction_amount'))['total'] or 0

    start_of_week = now - timedelta(days=now.weekday())
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59, microseconds=999999)

    total_amount_this_week = Transaction.objects.filter(transaction_date__gte=start_of_week, transaction_date__lte=end_of_week).aggregate(total=Sum('transaction_amount'))['total'] or 0

    response_data = {
        'total_amount':total_amount,
        'total_amount_this_week':total_amount_this_week
    }

    return Response(response_data)
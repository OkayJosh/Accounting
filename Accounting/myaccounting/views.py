from rest_framework import viewsets

from .serializers import IncomeSerializer, ExpenseSerializer, OtherFinancialsSerializer

from .models import Income, Expense, OtherFinancials

# Income View
class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()

# Income View
class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

# Other Finiancal View
class OtherFinancialsViewSet(viewsets.ModelViewSet):
    serializer_class = OtherFinancialsSerializer
    queryset = OtherFinancials.objects.all()
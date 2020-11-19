from rest_framework import serializers

from .models import Income, Expense, OtherFinancials

# Income Serializer
class IncomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Income
        fields = ['name', 'amount', 'comment']

# Expense Serializer
class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'comment']

# Other Financials Serializer
class OtherFinancialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OtherFinancials
        fields = ['name', 'amount', 'comment']
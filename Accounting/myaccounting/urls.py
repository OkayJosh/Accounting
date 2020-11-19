from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, OtherFinancialsViewSet

router = DefaultRouter()

# income route
router.register('income', IncomeViewSet, basename='acc-income')

# expense route
router.register('expense', ExpenseViewSet, basename='acc-expense')

# others route
router.register('others', OtherFinancialsViewSet, basename='acc-other')

urlpatterns = [
    
] + router.urls
from django.urls import path
from .views import TransactionListCreate, TransactionDetailView, UserListCreate

urlpatterns = [

    path("user/register/", UserListCreate.as_view(), name="register"),
    path("transactions/", TransactionListCreate.as_view(), name="transactions"),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    
]


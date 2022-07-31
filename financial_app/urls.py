from django.urls import path
from .views import ( User_Financial_data)

urlpatterns = [
    path(
        "user_financial_data/", User_Financial_data.as_view(), name="User_Financial_data"
    ),
]




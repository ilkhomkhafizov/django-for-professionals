from django.urls import path

from .views import OrdersViewPage, charge



urlpatterns = [
    path('charge/', charge, name='charge'),
    path('', OrdersViewPage.as_view(), name='orders'),
]

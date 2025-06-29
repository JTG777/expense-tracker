from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('remove-transaction/<int:pk>/',views.remove_transaction,name="remove_transaction"),
]
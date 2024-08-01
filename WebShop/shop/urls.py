from django.urls import path
from .views import ItemListCreateView, ItemDetailView, populate_db , ItemSearchView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('populate-db/', populate_db, name='populate-db'),
    path('search/', ItemSearchView.as_view(), name='item-search'),
]

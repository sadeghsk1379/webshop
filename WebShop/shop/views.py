from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from users.models import CustomUser
from django.http import JsonResponse
from django.db.models import Q
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemSearchView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Item.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))


def populate_db(request):
    Item.objects.all().delete()
    CustomUser.objects.filter(username__startswith='testuser').delete()

    for i in range(6):
        user = CustomUser.objects.create_user(
            username=f'testuser{i+1}', password=f'pass{i+1}', email=f'testuser{i+1}@shop.aa')
        if i < 3:
            for j in range(10):
                Item.objects.create(
                    title=f'Item {i+1}-{j+1}',
                    description=f'Description for item {i+1}-{j+1}',
                    price=10.0 * (j+1),
                    owner=user
                )
    return JsonResponse({'message': 'Database populated with test data'})

from rest_framework import generics


from .models import Imovel
from .serializers import ImovelSerializer

class ImovelListCreateAPIView(generics.ListCreateAPIView):
	queryset = Imovel.objects.all()
	serializer_class = ImovelSerializer

imoveis_list_create_view = ImovelListCreateAPIView.as_view()

class ImovelDetailAPIView(generics.RetrieveAPIView):
	queryset = Imovel.objects.all()
	serializer_class = ImovelSerializer
	# lookup_field = 'pk' (default_auto_field)

imovel_detail_view = ImovelDetailAPIView.as_view()

class ImovelUpdateAPIView(generics.UpdateAPIView):
	queryset = Imovel.objects.all()
	serializer_class = ImovelSerializer
	lookup_field = 'pk'

	def perform_update(self, serializer):
		return super().perform_update(serializer)

imovel_update_view = ImovelUpdateAPIView.as_view()

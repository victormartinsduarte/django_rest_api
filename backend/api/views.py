from rest_framework import generics


from .models import Imovel, Anuncio, Reserva
from .serializers import ImovelSerializer, AnuncioSerializer, ReservaSerializer

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

class ImovelDeleteAPIView(generics.DestroyAPIView):
	queryset = Imovel.objects.all()
	serializer_class = ImovelSerializer
	lookup_field = 'pk'

	def perform_destroy(self, instance):
		return super().perform_destroy(instance)

imovel_delete_view = ImovelDeleteAPIView.as_view()

class AnuncioListCreateAPIView(generics.ListCreateAPIView):
	queryset = Anuncio.objects.all()
	serializer_class = AnuncioSerializer

anuncios_list_create_view = AnuncioListCreateAPIView.as_view()

class AnuncioDetailAPIView(generics.RetrieveAPIView):
	queryset = Anuncio.objects.all()
	serializer_class = AnuncioSerializer

anuncio_detail_view = AnuncioDetailAPIView.as_view()

class AnuncioUpdateAPIView(generics.UpdateAPIView):
	queryset = Anuncio.objects.all()
	serializer_class = AnuncioSerializer
	lookup_field = 'pk'

	def perform_update(self, serializer):
		return super().perform_update(serializer)

anuncio_update_view = AnuncioUpdateAPIView.as_view()

class ReservaListCreateAPIView(generics.ListCreateAPIView):
	queryset = Reserva.objects.all()
	serializer_class = ReservaSerializer

reservas_list_create_view = ReservaListCreateAPIView.as_view()

class ReservaDetailAPIView(generics.RetrieveAPIView):
	queryset = Reserva.objects.all()
	serializer_class = ReservaSerializer

reserva_detail_view = ReservaDetailAPIView.as_view()

class ReservaDeleteAPIView(generics.DestroyAPIView):
	queryset = Reserva.objects.all()
	serializer_class = ReservaSerializer
	lookup_field = 'pk'

	def perform_destroy(self, instance):
		return super().perform_destroy(instance)

reserva_delete_view = ReservaDeleteAPIView.as_view()
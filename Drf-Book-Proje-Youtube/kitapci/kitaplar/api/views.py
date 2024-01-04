from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import generics
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from kitaplar.models import *
from kitaplar.api.serializers import *



class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

class YorumListCreateAPIView(generics.ListCreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get("kitap_pk")
        kitap = get_object_or_404(Kitap,pk=kitap_pk)
        serializer.save(kitap=kitap)

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer




# class KitapListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):

#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer

#     # Kitap Listeleme
#     def get(self,request,*args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # Kitap Oluşturma
#     def post(self,request,*args, **kwargs):
#         return self.create(request, *args, **kwargs)
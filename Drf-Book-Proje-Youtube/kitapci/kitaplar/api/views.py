from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from kitaplar.models import *
from kitaplar.api.serializers import *
from kitaplar.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
from kitaplar.api.pagination import *


class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all().order_by("-id")
    serializer_class = KitapSerializer
    permission_classes =[IsAdminUserOrReadOnly]
    pagination_class = LargePagination

class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes =[IsAdminUserOrReadOnly]

class YorumListCreateAPIView(generics.ListCreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get("kitap_pk")
        kitap = get_object_or_404(Kitap,pk=kitap_pk)
        yorumcu = self.request.user
        yorumlar = Yorum.objects.filter(kitap=kitap,yorumcu=yorumcu)
        if yorumlar.exists():
            raise ValidationError("Bir kitap'a birden fazla yorum yapamazsınız!")
        serializer.save(kitap=kitap,yorumcu=yorumcu)

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsYorumSahibiOrReadOnly]

    # def perform_update(self, serializer):
    #     girisli_kullanici = self.request.user
    #     yorum_sahibi = Yorum.objects.filter(yorumcu = girisli_kullanici)
    #     if yorum_sahibi.exists():
    #         raise ValidationError("Yorumu sadece yorum sahibi düzenleyebilir!")
    #     serializer.save()




# class KitapListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):

#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer

#     # Kitap Listeleme
#     def get(self,request,*args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # Kitap Oluşturma
#     def post(self,request,*args, **kwargs):
#         return self.create(request, *args, **kwargs)
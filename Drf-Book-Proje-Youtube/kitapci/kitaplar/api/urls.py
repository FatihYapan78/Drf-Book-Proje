from django.urls import path
from kitaplar.api.views import *
urlpatterns = [
    path("kitaplar/", KitapListCreateAPIView.as_view(), name="kitap-listesi"),
    path("kitaplar/<int:pk>", KitapDetailAPIView.as_view(), name="kitap-detay"),
    path("kitaplar/<int:kitap_pk>/yorum_yap", YorumListCreateAPIView.as_view(), name="yorum-yap"),
    path("yorumlar/", YorumListCreateAPIView.as_view(), name="yorumlar"),
    path("yorumlar/<int:pk>", YorumDetailAPIView.as_view(), name="yorum-detay"),
]
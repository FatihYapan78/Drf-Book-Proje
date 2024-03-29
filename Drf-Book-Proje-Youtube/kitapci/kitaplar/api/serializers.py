from rest_framework import serializers
from kitaplar.models import *

class YorumSerializer(serializers.ModelSerializer):
    yorumcu = serializers.StringRelatedField(read_only=True)
    class Meta: 
        model = Yorum
        # fields = "__all__"
        exclude = ["kitap"]

class KitapSerializer(serializers.ModelSerializer):
    yorumlar = YorumSerializer(many=True,read_only=True)
    class Meta: 
        model = Kitap
        fields = "__all__"
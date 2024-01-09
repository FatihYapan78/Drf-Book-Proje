import os
import random
import requests
os.environ.setdefault("DJAGO_SETTINGS_MODULE","kitapci.settings")

import django
django.setup()
# Modellerimize ulaşabilmek için 
from django.contrib.auth.models import User
from kitaplar.api.serializers import *
from faker import Faker

def set_user():
    fake = Faker(["tr_TR"])

    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name}_{l_name}'
    email = f'{u_name}@{fake.domain_name()}'
    print(f_name,l_name,email)
    user_check = User.objects.filter(username=u_name)

    while user_check.exists():
        u_name = u_name + str(random.randrange(1,99))
        user_check = User.objects.filter(username=u_name)

    user = User(
    username = u_name,
    first_name = f_name,
    last_name = l_name,
    email = email,
    # is_staff = fake.boolean(chance_of_getting_true=50)
    )

    user.set_password("test123")
    user.save()

def kitap_ekle(konu):
    fake = Faker(["tr_TR"])
    response = requests.get(f"https://openlibrary.org/search.json?q={konu}")
    
    jsn = response.json()
    kitaplar = jsn.get("docs")

    for kitap in kitaplar:
        data = {
            "isim" : kitap.get("title"),
            "yazar" : kitap.get("author_name")[0],
            "aciklama" : kitap.get("title"),
            "yayin_tarihi" : fake.date_time_between(start_date = '-20y', end_date = 'now', tzinfo = None)
        }

        serializer = KitapSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
        else:
            continue






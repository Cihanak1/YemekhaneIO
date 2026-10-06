# -*- coding: utf-8 -*-
import json

breakfast_data = {
    "baslik": "EKİM AYI KAHVALTI MENÜSÜ",
    "ay": "Ekim 2026",
    "notlar": [
        "*Siyah/Yeşil Zeytin verilen günlerde her iki çeşit de bulundurulacaktır.",
        "**Çay/Bitki Çayından her ikisi de bulundurulacaktır. Öğrenci istediği çeşitten sadece birini alacaktır.",
        "NOT 1: Reçel çeşitleri, sürülebilir çikolata, bal, tereyağ, tahinli pekmez, helva, labne, krem peynir, üçgen peynir piknik ürün olacaktır."
    ],
    "imza": {
        "isim": "Abdulsamet EREN",
        "unvan": "Gençlik ve Spor İl Müdürü"
    },
    "gunler": {
        "01.10.2026": {
            "tarih": "01.10.2026",
            "gun": "Perşembe",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kavurma", "Karışık Pizza", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kavurma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Karışık Pizza", "gramaj": "150 g", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "02.10.2026": {
            "tarih": "02.10.2026",
            "gun": "Cuma",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Menemen", "Patates Kızartma", "Çikolatalı Kek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Menemen", "gramaj": "150 g (1 adet L boy yumurta)", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Çikolatalı Kek", "gramaj": "60 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "03.10.2026": {
            "tarih": "03.10.2026",
            "gun": "Cumartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Karışık Kızartma", "Simit", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Simit", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "04.10.2026": {
            "tarih": "04.10.2026",
            "gun": "Pazar",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sade Omlet", "Salçalı Sosis", "Peynirli Börek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sade Omlet", "gramaj": "1 adet L boy yumurta", "enerji": ""},
                {"ad": "Salçalı Sosis", "gramaj": "100 g", "enerji": ""},
                {"ad": "Peynirli Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "05.10.2026": {
            "tarih": "05.10.2026",
            "gun": "Pazartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kızartma", "Zeytinli/Peynirli Açma", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Zeytinli/Peynirli Açma", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "06.10.2026": {
            "tarih": "06.10.2026",
            "gun": "Salı",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Kaşarlı Omlet", "Patates Salata", "Dere Otlu Poğaça", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Kaşarlı Omlet", "gramaj": "25 g kaşar p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Salata", "gramaj": "150 g", "enerji": ""},
                {"ad": "Dere Otlu Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "07.10.2026": {
            "tarih": "07.10.2026",
            "gun": "Çarşamba",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Sosis Kızartma", "Ispanaklı Börek", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Sosis Kızartma", "gramaj": "100 g", "enerji": ""},
                {"ad": "Ispanaklı Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "08.10.2026": {
            "tarih": "08.10.2026",
            "gun": "Perşembe",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sucuklu Omlet", "Karışık Kızartma", "Kakaolu Kek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sucuklu Omlet", "gramaj": "1 adet L boy yumurta+ 25 g beyaz etli sucuk", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Kakaolu Kek", "gramaj": "60 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "09.10.2026": {
            "tarih": "09.10.2026",
            "gun": "Cuma",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kızartması", "Kek+ Bal+Tereyağ", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kızartması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Kek+ Bal+Tereyağ", "gramaj": "50+20 g+10 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "10.10.2026": {
            "tarih": "10.10.2026",
            "gun": "Cumartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Peynirli Omlet", "Patates Kavurması", "Peynirli Börek", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Peynirli Omlet", "gramaj": "30 g beyaz p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Kavurması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Peynirli Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "11.10.2026": {
            "tarih": "11.10.2026",
            "gun": "Pazar",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kızartma", "Karışık Pizza", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Karışık Pizza", "gramaj": "150 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "12.10.2026": {
            "tarih": "12.10.2026",
            "gun": "Pazartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sade Omlet", "Patates Kızartma", "Çikolatalı Kek", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sade Omlet", "gramaj": "1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Çikolatalı Kek", "gramaj": "60 g", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "13.10.2026": {
            "tarih": "13.10.2026",
            "gun": "Salı",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Salçalı Sosis", "Sade Poğaça", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Salçalı Sosis", "gramaj": "100 g", "enerji": ""},
                {"ad": "Sade Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "14.10.2026": {
            "tarih": "14.10.2026",
            "gun": "Çarşamba",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Kaşarlı Omlet", "Karışık Kızartma", "Zeytinli/Peynirli Açma", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Kaşarlı Omlet", "gramaj": "25 g kaşar p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Zeytinli/Peynirli Açma", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "15.10.2026": {
            "tarih": "15.10.2026",
            "gun": "Perşembe",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Salata", "Sürülebilir Çikolata+ Kek", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Salata", "gramaj": "150 g", "enerji": ""},
                {"ad": "Sürülebilir Çikolata+ Kek", "gramaj": "20 g +50gr", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "16.10.2026": {
            "tarih": "16.10.2026",
            "gun": "Cuma",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Menemen", "Patates Kızartma", "Simit", "Krem Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Menemen", "gramaj": "150 g (1 adet L boy yumurta)", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Simit", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Krem Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "17.10.2026": {
            "tarih": "17.10.2026",
            "gun": "Cumartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Karışık Kızartma", "Peynirli Börek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Peynirli Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "18.10.2026": {
            "tarih": "18.10.2026",
            "gun": "Pazar",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sucuklu Omlet", "Patates Kavurma", "Dere Otlu Poğaça", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sucuklu Omlet", "gramaj": "1 adet L boy yumurta+ 25 g beyaz etli sucuk", "enerji": ""},
                {"ad": "Patates Kavurma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Dere Otlu Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "19.10.2026": {
            "tarih": "19.10.2026",
            "gun": "Pazartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Sosis Kızartma", "Reçel", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Sosis Kızartma", "gramaj": "100 g", "enerji": ""},
                {"ad": "Reçel", "gramaj": "20 g", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "20.10.2026": {
            "tarih": "20.10.2026",
            "gun": "Salı",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Peynirli Omlet", "Patates Kızartma", "Karışık Pizza", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Peynirli Omlet", "gramaj": "30 g beyaz p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Karışık Pizza", "gramaj": "150 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "21.10.2026": {
            "tarih": "21.10.2026",
            "gun": "Çarşamba",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Karışık Kızartma", "Sade Poğaça", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Sade Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "22.10.2026": {
            "tarih": "22.10.2026",
            "gun": "Perşembe",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sade Omlet", "Patates Salata", "Çikolatalı Kek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sade Omlet", "gramaj": "1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Salata", "gramaj": "150 g", "enerji": ""},
                {"ad": "Çikolatalı Kek", "gramaj": "60 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "23.10.2026": {
            "tarih": "23.10.2026",
            "gun": "Cuma",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kızartma", "Peynirli Börek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Peynirli Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "24.10.2026": {
            "tarih": "24.10.2026",
            "gun": "Cumartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Kaşarlı Omlet", "Karışık Kızartma", "Sucuklu Yumurta", "Krem Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Kaşarlı Omlet", "gramaj": "25 g kaşar p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Sucuklu Yumurta", "gramaj": "1 adet L boy yumurta+ 25 g beyaz etli sucuk", "enerji": ""},
                {"ad": "Krem Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "25.10.2026": {
            "tarih": "25.10.2026",
            "gun": "Pazar",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Sosis Kızartma", "Simit", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Sosis Kızartma", "gramaj": "100 g", "enerji": ""},
                {"ad": "Simit", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "26.10.2026": {
            "tarih": "26.10.2026",
            "gun": "Pazartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sucuklu Omlet", "Patates Salatası", "Dere Otlu Poğaça", "Krem Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sucuklu Omlet", "gramaj": "1 adet L boy yumurta+ 25 g beyaz etli sucuk", "enerji": ""},
                {"ad": "Patates Salatası", "gramaj": "150 g", "enerji": ""},
                {"ad": "Dere Otlu Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Krem Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "27.10.2026": {
            "tarih": "27.10.2026",
            "gun": "Salı",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kızartma", "Kek+ Bal+Tereyağ", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Kek+ Bal+Tereyağ", "gramaj": "50g+20 g+10 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "28.10.2026": {
            "tarih": "28.10.2026",
            "gun": "Çarşamba",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sucuklu Omlet", "Patates Kavurma", "Zeytinli/Peynirli Açma", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sucuklu Omlet", "gramaj": "1 adet L boy yumurta+ 25 g beyaz etli sucuk", "enerji": ""},
                {"ad": "Patates Kavurma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Zeytinli/Peynirli Açma", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "29.10.2026": {
            "tarih": "29.10.2026",
            "gun": "Perşembe",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Menemen", "Karışık Kızartma", "Mozaik Kek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Menemen", "gramaj": "150 g (1 adet L boy yumurta)", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Mozaik Kek", "gramaj": "60 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "30.10.2026": {
            "tarih": "30.10.2026",
            "gun": "Cuma",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sade Omlet", "Patates Kızartma", "Simit", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sade Omlet", "gramaj": "1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Simit", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "31.10.2026": {
            "tarih": "31.10.2026",
            "gun": "Cumartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Salçalı Sosis", "Ispanaklı Börek", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Salçalı Sosis", "gramaj": "100 g", "enerji": ""},
                {"ad": "Ispanaklı Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        }
    }
}

for v in breakfast_data["gunler"].values():
    v["foods"] = v["yemekler"]

breakfast_data["liste"] = list(breakfast_data["gunler"].values())

with open('data/sabah_kahvaltisi.json', 'w', encoding='utf-8') as f:
    json.dump(breakfast_data, f, ensure_ascii=False, indent=2)
print("Sabah kahvaltisi JSON yazildi. Toplam gun:", len(breakfast_data["gunler"]))


dinner_data = {
    "baslik": "EKİM AYI AKŞAM YEMEĞİ MENÜ TASLAĞI",
    "ay": "Ekim 2026",
    "notlar": [
        "Not: (02.10-16.10) Tarihlerinde Ahmet Kabaklı, (05.10-22.10) Sare Ana, Harput, İzzetpaşa (11.10-27.10) Ömer Bilginoğlu, Fethi Sekin, Fırat, yurtlarımızda (Mercimek çorba, Lahmacun, Mevsim Salata, Ayran) menüsü verilecektir."
    ],
    "imza": {
        "isim": "Abdulsamet EREN",
        "unvan": "Gençlik ve Spor İl Müdürü"
    },
    "gunler": {
        "01.10.2026": {
            "tarih": "01.10.2026",
            "gun": "Perşembe",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorbası / Şehriye Çorbası",
                "Tavuk Döner(%90) / Karışık Sebze Graten",
                "Pirinç Pilavı",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorbası / Şehriye Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Döner(%90)/Karışık Sebze Graten", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "02.10.2026": {
            "tarih": "02.10.2026",
            "gun": "Cuma",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Domates Çorbası / Yayla Çorbası",
                "Etsiz Kuru Fasülye / Kabak Kalye / Tavuk Fajita",
                "Şehriyeli Bulgur Pilavı",
                "Haydari",
                "Puding"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Domates Çorbası / Yayla Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Etsiz Kuru Fasülye /Kabak kalye//Tavuk Fajita", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Şehriyeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Haydari", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Puding", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "03.10.2026": {
            "tarih": "03.10.2026",
            "gun": "Cumartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorbası / Düğün Çorbası",
                "Tas Kebabı / Şinitzel / İmam Bayıldı",
                "Pirinç Pilavı",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorbası / Düğün Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tas Kebabı / Şinitzel/ İmam Bayıldı", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "04.10.2026": {
            "tarih": "04.10.2026",
            "gun": "Pazar",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin Çorbası / Tutmaç Çorbası",
                "Fırında Tavuk Biftek / Mücver / Etli Dolma",
                "Salçalı Makarna",
                "Tarator"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin Çorbası / Tutmaç Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Fırında Tavuk Biftek/Mücver/Etli Dolma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Salçalı Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Tarator", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "05.10.2026": {
            "tarih": "05.10.2026",
            "gun": "Pazartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Terbiyeli Sebze Çorbası / Domates Çorbası",
                "Çiftlik Köfte / Nugget / Taze Fasülye",
                "Yeşil Mercimekli Bulgur Pilavı",
                "Şekerpare"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Terbiyeli Sebze Çorbası / Domates Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Çiftlik Köfte/Nugget/ Taze Fasülye", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Yeşil Mercimekli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Şekerpare", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "06.10.2026": {
            "tarih": "06.10.2026",
            "gun": "Salı",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorbası / Ayran Aşı",
                "Tavuk Kavurma / Mantı / Arap Tava",
                "Nohutlu Pirinç Pilavı",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorbası / Ayran Aşı", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Kavurma/Mantı/Arap Tava", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Nohutlu Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "07.10.2026": {
            "tarih": "07.10.2026",
            "gun": "Çarşamba",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Şehriye Çorbası / Yayla Çorbası",
                "Karnıyarık / Tavuk Tantuni / Karışık Kızartma",
                "Fırın Makarna",
                "Cacık"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Şehriye Çorbası / Yayla Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Karnıyarık/Tavuk Tantuni/ Karışık Kızartma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Fırın Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Cacık", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "08.10.2026": {
            "tarih": "08.10.2026",
            "gun": "Perşembe",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Düğün Çorbası / Şehriye Çorbası",
                "Fırın Tavuk Baget / Kabak Kalye / Etli Taze Fasülye",
                "Sebzeli Bulgur Pilavı",
                "Sütlaç"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Düğün Çorbası / Şehriye Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Fırın Tavuk Baget/Kabak Kalye/Etli Taze Fasülye", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sebzeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Sütlaç", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "09.10.2026": {
            "tarih": "09.10.2026",
            "gun": "Cuma",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorbası / Mısır Çorbası",
                "Orman Kebabı / Tavuk Şiş / Yoğurtlu Mantı",
                "Pirinç Pilavı",
                "Pembe Sultan"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorbası / Mısır Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Orman Kebabı / Tavuk Şiş/Yoğurtlu Mantı", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Pembe Sultan", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "10.10.2026": {
            "tarih": "10.10.2026",
            "gun": "Cumartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Süzme Mercimek Çorbası / Yayla Çorbası",
                "Çıtır Tavuk+Patates Kızartması / Mücver / Fırında Dizme Köfte",
                "Domates Soslu Makarna",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Süzme Mercimek Çorbası / Yayla Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Çıtır Tavuk+Patates Kızartması/Mücver/Fırında Dizme Köfte", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Domates Soslu Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "11.10.2026": {
            "tarih": "11.10.2026",
            "gun": "Pazar",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Terbiyeli Sebze Çorbası / Şehriye Çorbası",
                "Etsiz Kuru Fasülye / Karışık Dolma / Tavuk Baget Kızartma",
                "Erişte Pilavı",
                "Cevizli Baklava"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Terbiyeli Sebze Çorbası / Şehriye Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Etsiz Kuru Fasülye /Karışık Dolma/ Tavuk Baget Kızartma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Erişte Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Cevizli Baklava", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "12.10.2026": {
            "tarih": "12.10.2026",
            "gun": "Pazartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorbası / Ayran Aşı",
                "Kavurma / Sulu Nohut / Tavuk Çöp Şiş",
                "Pirinç Pilavı",
                "Karışık Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorbası / Ayran Aşı", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Kavurma / Sulu Nohut/Tavuk Çöp Şiş", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Karışık Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "13.10.2026": {
            "tarih": "13.10.2026",
            "gun": "Salı",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorbası / Domates Çorbası",
                "Fırında Tavuk Baget / Karışık Sebze Graten / Patlıcan Musakka",
                "Nohutlu Pirinç Pilavı",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorbası / Domates Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Fırında Tavuk Baget/Karışık Sebze Graten/Patlıcan Musakka", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Nohutlu Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "14.10.2026": {
            "tarih": "14.10.2026",
            "gun": "Çarşamba",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin Çorbası / Tutmaç Çorbası",
                "Hamburger Köfte+Patates / Tavuk Burger / Bezelye Yemeği",
                "Soslu Makarna",
                "Ayran"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin Çorbası / Tutmaç Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Hamburger Köfte+Patates /Tavuk Burger/ Bezelye Yemeği", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Soslu Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Ayran", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "15.10.2026": {
            "tarih": "15.10.2026",
            "gun": "Perşembe",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorba / Mısır Çorba",
                "Tavuk Fajita / Yoğurtlu Mantı / Kilis Tava",
                "Yeşil Mercimekli Bulgur Pilavı",
                "Çoban Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorba/Mısır Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Fajita/Yoğurtlu Mantı/Kilis Tava", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Yeşil Mercimekli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Çoban Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "16.10.2026": {
            "tarih": "16.10.2026",
            "gun": "Cuma",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ayran Aşı Çorba / Ezogelin Çorbası",
                "Etsiz Kuru Fasülye / Mevsim Soslu Karışık Kızartma / Tavuk Külbastı",
                "Mısırlı Pirinç Pilavı",
                "Rus Salatası",
                "Revani"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ayran Aşı Çorba / Ezogelin Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Etsiz Kuru Fasülye/Mevsim Soslu Karışık Kızartma/Tavuk Külbastı", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Mısırlı Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Rus Salatası", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Revani", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "17.10.2026": {
            "tarih": "17.10.2026",
            "gun": "Cumartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Sebze Çorbası / Tarhana Çorbası",
                "Tavuk Tantuni / Bezelye Yemeği / Patlıcan Musakka",
                "Salçalı Makarna",
                "Ayran"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Sebze Çorbası / Tarhana Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Tantuni /Bezelye Yemeği/Patlıcan Musakka", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Salçalı Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Ayran", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "18.10.2026": {
            "tarih": "18.10.2026",
            "gun": "Pazar",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ayran Aşı Çorbası / Mercimek Çorbası",
                "Güveç / Çıtır Tavuk / Ispanak Kavurma",
                "Sebzeli Bulgur Pilavı",
                "Cacık"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ayran Aşı Çorbası / Mercimek Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Güveç/Çıtır Tavuk /Ispanak Kavurma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sebzeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Cacık", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "19.10.2026": {
            "tarih": "19.10.2026",
            "gun": "Pazartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorbası / Mercimek Çorbası",
                "Tavuk Kavurma / Karışık Soslu Sebze Kızartma / Çiftlik Kebabı",
                "Fırın Makarna",
                "Cevizli Baklava"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorbası / Mercimek Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Kavurma/Karışık Soslu Sebze Kızartma/Çiftlik Kebabı", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Fırın Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Cevizli Baklava", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "20.10.2026": {
            "tarih": "20.10.2026",
            "gun": "Salı",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin Çorbası / Sebze Çorbası",
                "Hamburger Köfte+Patates / Tavuk Burger / Taze Fasülye",
                "Pirinç Pilavı",
                "Ayran"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin Çorbası / Sebze Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Hamburger Köfte+Patates /Tavuk Burger/ Taze Fasülye", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Ayran", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "21.10.2026": {
            "tarih": "21.10.2026",
            "gun": "Çarşamba",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Sebze Çorbası / Mercimek Çorbası",
                "Fırında Sebzeli Tavuk Izgara / Mevsim Türlü / Etli Dolma",
                "Soslu Makarna",
                "Karışık Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Sebze Çorbası / Mercimek Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Fırında Sebzeli Tavuk Izgara/Mevsim Türlü/Etli Dolma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Soslu Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Karışık Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "22.10.2026": {
            "tarih": "22.10.2026",
            "gun": "Perşembe",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Yayla Çorbası / Şehriye Çorbası",
                "Etsiz Kuru Fasülye / Mevsim Soslu Karışık Kızartma // Tavuk Çöp Şiş",
                "Bulgur Pilavı",
                "Haydari",
                "Tulumba"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Yayla Çorbası / Şehriye Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Etsiz Kuru Fasülye /Mevsim Soslu Karışık Kızartma//Tavuk Çöp Şiş", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Haydari", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Tulumba", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "23.10.2026": {
            "tarih": "23.10.2026",
            "gun": "Cuma",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin / Domates Çorbası",
                "Patlıcan Musakka / Nugget / Yoğurtlu Kabak",
                "Soslu Makarna",
                "Karışık Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin / Domates Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Patlıcan Musakka /Nugget/ Yoğurtlu Kabak", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Soslu Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Karışık Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "24.10.2026": {
            "tarih": "24.10.2026",
            "gun": "Cumartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ayran Aşı Çorbası / Tarhana Çorbası",
                "Şinitzel / Rosto Köfte / Sulu Patates",
                "Erişte Pilavı",
                "Şekerpare"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ayran Aşı Çorbası / Tarhana Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Şinitzel/Rosto Köfte/Sulu Patates", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Erişte Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Şekerpare", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "25.10.2026": {
            "tarih": "25.10.2026",
            "gun": "Pazar",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Yayla Çorbası / Ezogelin Çorbası",
                "Patlıcan Parmak Kebabı / Salçalı Mantı / Tavuk Baget Kızartma",
                "Bulgur Pilavı",
                "Ezme"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Yayla Çorbası / Ezogelin Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Patlıcan Parmak Kebabı / Salçalı Mantı/Tavuk Baget Kızartma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Ezme", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "26.10.2026": {
            "tarih": "26.10.2026",
            "gun": "Pazartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Şehriye Çorbası / Mercimek Çorbası",
                "Tavuk Döner(%90) / Karışık Sebze Graten",
                "Pirinç Pilavı",
                "Karışık Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Şehriye Çorbası / Mercimek Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Döner(%90)/Karışık Sebze Graten", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Karışık Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "27.10.2026": {
            "tarih": "27.10.2026",
            "gun": "Salı",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Sebze Çorbası / Tarhana Çorbası",
                "Etsiz Kuru Fasülye / Mevsim Soslu Karışık Kızartma / Nugget",
                "Erişte Pilavı",
                "Yoğurt",
                "Browni"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Sebze Çorbası / Tarhana Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Etsiz Kuru Fasülye/Mevsim Soslu Karışık Kızartma/Nugget", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Erişte Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Yoğurt", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Browni", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "28.10.2026": {
            "tarih": "28.10.2026",
            "gun": "Çarşamba",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorbası / Domates Çorbası",
                "Kuşbaşılı Patlıcan Kebap / Tavuk Kavurma / Bezelye Yemeği",
                "Sebzeli Bulgur Pilavı",
                "Çoban Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorbası / Domates Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Kuşbaşılı Patlıcan Kebap/ Tavuk kavurma /Bezelye Yemeği", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sebzeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Çoban Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "29.10.2026": {
            "tarih": "29.10.2026",
            "gun": "Perşembe",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin Çorba / Tarhana Çorba",
                "Tavuk Tantuni / Mücver / Kıymalı Ispanak",
                "Makarna Salatası",
                "Ayran"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin Çorba / Tarhana Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Tantuni/Mücver/Kıymalı Ispanak", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Makarna Salatası", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Ayran", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "30.10.2026": {
            "tarih": "30.10.2026",
            "gun": "Cuma",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorba / Yayla Çorbası",
                "Ekmek Arası Köfte / Tavuk Sote / Yoğurtlu Mantı",
                "Nohutlu Pirinç Pilavı",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorba/ Yayla Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Ekmek Arası Köfte/ Tavuk Sote /Yoğurtlu Mantı", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Nohutlu Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "31.10.2026": {
            "tarih": "31.10.2026",
            "gun": "Cumartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Dövme Çorba / Domates Çorbası",
                "Orman Kebap / Ispanak Yemeği / Tavuk Çöp Şiş",
                "Bulgur Pilavı",
                "Sütlaç"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Dövme Çorba/ Domates Çorbası", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Orman Kebap/Ispanak Yemeği/ Tavuk Çöp Şiş", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Sütlaç", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        }
    }
}

for v in dinner_data["gunler"].values():
    v["foods"] = v["yemekler"]

dinner_data["liste"] = list(dinner_data["gunler"].values())

with open('data/aksam_yemegi.json', 'w', encoding='utf-8') as f:
    json.dump(dinner_data, f, ensure_ascii=False, indent=2)
print("Aksam yemegi JSON yazildi. Toplam gun:", len(dinner_data["gunler"]))


# ── Çalışma zamanı paketi (data/*.js) ─────────────────────────────
# Tarayıcı file:// ile açıldığında fetch() engellenir; bu yüzden aynı veri
# bir <script> ile global değişken olarak da yüklenir. Paket yalnızca
# arayüzün ihtiyaç duyduğu alanları içerir ve sıkıştırılmış (minified) yazılır.
def build_runtime_bundle(data, global_name, out_path):
    def slim_item(o):
        item = {"ad": o["ad"]}
        for key in ("gramaj", "enerji", "kategori"):
            if o.get(key):
                item[key] = o[key]
        return item

    compact = {
        "baslik": data["baslik"],
        "notlar": data["notlar"],
        "imza": data["imza"],
        "gunler": {
            tarih: {
                "gun": gun["gun"],
                "yemekler": gun["yemekler"],
                "ogeler": [slim_item(o) for o in gun["ogeler"]],
            }
            for tarih, gun in data["gunler"].items()
        },
    }
    payload = json.dumps(compact, ensure_ascii=False, separators=(",", ":"))
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("/* Otomatik üretildi: convert_menus.py — elle düzenlemeyin. */\n")
        f.write(f"window.{global_name}={payload};\n")
    print(f"{out_path} yazildi ({len(payload.encode('utf-8')) // 1024} KB)")


build_runtime_bundle(breakfast_data, "MENU_DATA_SABAH", "data/sabah_kahvaltisi.js")
build_runtime_bundle(dinner_data, "MENU_DATA_AKSAM", "data/aksam_yemegi.js")

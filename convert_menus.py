# -*- coding: utf-8 -*-
import json

breakfast_data = {
    "baslik": "KASIM AYI KAHVALTI MENÜSÜ",
    "ay": "Kasım 2026",
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
        "01.11.2026": {
            "tarih": "01.11.2026",
            "gun": "Pazar",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Peynirli Omlet", "Sosis Kızartma", "Sade Poğaça", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Peynirli Omlet", "gramaj": "30 g beyaz p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Sosis Kızartma", "gramaj": "100 gr", "enerji": ""},
                {"ad": "Sade Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "02.11.2026": {
            "tarih": "02.11.2026",
            "gun": "Pazartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kızartması", "Zeytinli/Peynirli Açma", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kızartması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Zeytinli/Peynirli Açma", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "03.11.2026": {
            "tarih": "03.11.2026",
            "gun": "Salı",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Kaşarlı Omlet", "Patates Kızartma", "Dere Otlu Poğaça", "Krem Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Kaşarlı Omlet", "gramaj": "25 g kaşar p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Kızartma", "gramaj": "150 gr", "enerji": ""},
                {"ad": "Dere Otlu Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Krem Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "04.11.2026": {
            "tarih": "04.11.2026",
            "gun": "Çarşamba",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Sosis Kızartma", "Peynirli/Ispanaklı Börek", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Sosis Kızartma", "gramaj": "100 g", "enerji": ""},
                {"ad": "Peynirli/Ispanaklı Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "05.11.2026": {
            "tarih": "05.11.2026",
            "gun": "Perşembe",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sucuklu Omlet", "Karışık Kızartma", "Simit", "Krem Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sucuklu Omlet", "gramaj": "1 adet L boy yumurta+ 25 g beyaz etli sucuk", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Simit", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Krem Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "06.11.2026": {
            "tarih": "06.11.2026",
            "gun": "Cuma",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Haşlanmış Patates+Domates-Salatalık", "Karışık Pizza", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Haşlanmış Patates+Domates-Salatalık", "gramaj": "150 g+100 g", "enerji": ""},
                {"ad": "Karışık Pizza", "gramaj": "150 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "07.11.2026": {
            "tarih": "07.11.2026",
            "gun": "Cumartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Menemen", "Salçalı Sosis", "Patatesli Börek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Menemen", "gramaj": "150 g (1 adet L boy yumurta)", "enerji": ""},
                {"ad": "Salçalı Sosis", "gramaj": "100 gr", "enerji": ""},
                {"ad": "Patatesli Börek", "gramaj": "60 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "08.11.2026": {
            "tarih": "08.11.2026",
            "gun": "Pazar",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kavurması", "Kek + Sürülebilir Çikolata", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kavurması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Kek + Sürülebilir Çikolata", "gramaj": "60 g + 20 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "09.11.2026": {
            "tarih": "09.11.2026",
            "gun": "Pazartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sade Omlet", "Patates Kızartması", "Sade Poğaça", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sade Omlet", "gramaj": "1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Kızartması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Sade Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "10.11.2026": {
            "tarih": "10.11.2026",
            "gun": "Salı",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Salçalı Sosis", "Peynirli/Ispanaklı Börek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Salçalı Sosis", "gramaj": "100 g", "enerji": ""},
                {"ad": "Peynirli/Ispanaklı Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "11.11.2026": {
            "tarih": "11.11.2026",
            "gun": "Çarşamba",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Peynirli Omlet", "Karışık Kızartma", "Zeytinli/Peynirli Açma", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Peynirli Omlet", "gramaj": "30 g beyaz p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 gr", "enerji": ""},
                {"ad": "Zeytinli/Peynirli Açma", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "12.11.2026": {
            "tarih": "12.11.2026",
            "gun": "Perşembe",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kızartması", "Domates-Salatalık", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kızartması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Domates-Salatalık", "gramaj": "100 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "13.11.2026": {
            "tarih": "13.11.2026",
            "gun": "Cuma",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Menemen", "Patates Salatası", "Simit", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Menemen", "gramaj": "150 g (1 adet L boy yumurta)", "enerji": ""},
                {"ad": "Patates Salatası", "gramaj": "150 g", "enerji": ""},
                {"ad": "Simit", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "14.11.2026": {
            "tarih": "14.11.2026",
            "gun": "Cumartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Salçalı Sosis", "Ispanaklı Börek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Salçalı Sosis", "gramaj": "100 gr", "enerji": ""},
                {"ad": "Ispanaklı Börek", "gramaj": "60 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "15.11.2026": {
            "tarih": "15.11.2026",
            "gun": "Pazar",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sucuklu Omlet", "Patates Kızartması", "Dere Otlu Poğaça", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sucuklu Omlet", "gramaj": "1 adet L boy yumurta+ 25 g beyaz etli sucuk", "enerji": ""},
                {"ad": "Patates Kızartması", "gramaj": "150g", "enerji": ""},
                {"ad": "Dere Otlu Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "16.11.2026": {
            "tarih": "16.11.2026",
            "gun": "Pazartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kızartması", "Sade Poğaça", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kızartması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Sade Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "17.11.2026": {
            "tarih": "17.11.2026",
            "gun": "Salı",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Peynirli Omlet", "Sosis Kızartma", "Simit", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Peynirli Omlet", "gramaj": "30 g beyaz p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Sosis Kızartma", "gramaj": "100 gr", "enerji": ""},
                {"ad": "Simit", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "18.11.2026": {
            "tarih": "18.11.2026",
            "gun": "Çarşamba",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kavurması", "Karışık Pizza", "Krem Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kavurması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Karışık Pizza", "gramaj": "150 g", "enerji": ""},
                {"ad": "Krem Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "19.11.2026": {
            "tarih": "19.11.2026",
            "gun": "Perşembe",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sade Omlet", "Sosis Kızartma+ Domates-Salatalık", "Kek +Reçel", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sade Omlet", "gramaj": "1 adet L boy yumurta", "enerji": ""},
                {"ad": "Sosis Kızartma+ Domates-Salatalık", "gramaj": "100 g+100 g", "enerji": ""},
                {"ad": "Kek +Reçel", "gramaj": "60 g+ 20 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "20.11.2026": {
            "tarih": "20.11.2026",
            "gun": "Cuma",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Karışık Kızartma", "Zeytinli/Peynirli Açma", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 g", "enerji": ""},
                {"ad": "Zeytinli/Peynirli Açma", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "21.11.2026": {
            "tarih": "21.11.2026",
            "gun": "Cumartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Kaşarlı Omlet", "Patates Salatası", "Peynirli Börek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Kaşarlı Omlet", "gramaj": "25 g kaşar p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Salatası", "gramaj": "150 g", "enerji": ""},
                {"ad": "Peynirli Börek", "gramaj": "60 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "22.11.2026": {
            "tarih": "22.11.2026",
            "gun": "Pazar",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Sosis Kızartma", "Peynirli/Ispanaklı Börek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Sosis Kızartma", "gramaj": "100 gr", "enerji": ""},
                {"ad": "Peynirli/Ispanaklı Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "23.11.2026": {
            "tarih": "23.11.2026",
            "gun": "Pazartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Peynirli Omlet", "Patates Kızartması", "Dere Otlu Poğaça", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Peynirli Omlet", "gramaj": "30 g beyaz p.+ 1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Kızartması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Dere Otlu Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "24.11.2026": {
            "tarih": "24.11.2026",
            "gun": "Salı",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Salçalı Sosis", "Simit", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Salçalı Sosis", "gramaj": "100 g", "enerji": ""},
                {"ad": "Simit", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "25.11.2026": {
            "tarih": "25.11.2026",
            "gun": "Çarşamba",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sucuklu Omlet", "Karışık Kızartma", "Mozaik Kek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sucuklu Omlet", "gramaj": "1 adet L boy yumurta+ 25 g beyaz etli sucuk", "enerji": ""},
                {"ad": "Karışık Kızartma", "gramaj": "150 gr", "enerji": ""},
                {"ad": "Mozaik Kek", "gramaj": "50 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "26.11.2026": {
            "tarih": "26.11.2026",
            "gun": "Perşembe",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Kavurması", "Zeytinli/Peynirli Açma", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Kavurması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Zeytinli/Peynirli Açma", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "27.11.2026": {
            "tarih": "27.11.2026",
            "gun": "Cuma",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Sade Omlet", "Patates Kızartması", "Kek+ Bal", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Sade Omlet", "gramaj": "1 adet L boy yumurta", "enerji": ""},
                {"ad": "Patates Kızartması", "gramaj": "150g", "enerji": ""},
                {"ad": "Kek+ Bal", "gramaj": "60 g+ 20 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "28.11.2026": {
            "tarih": "28.11.2026",
            "gun": "Cumartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta+ Domates Salatalık", "Salçalı Sosis", "Peynirli/Ispanaklı Börek", "Labne Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta+ Domates Salatalık", "gramaj": "1 adet L boy+100 g", "enerji": ""},
                {"ad": "Salçalı Sosis", "gramaj": "100 g", "enerji": ""},
                {"ad": "Peynirli/Ispanaklı Börek", "gramaj": "120 g", "enerji": ""},
                {"ad": "Labne Peynir", "gramaj": "20 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "29.11.2026": {
            "tarih": "29.11.2026",
            "gun": "Pazar",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Menemen", "Patates Kızartması", "Peynirli Börek", "Beyaz Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Menemen", "gramaj": "150 g (1 adet L boy yumurta)", "enerji": ""},
                {"ad": "Patates Kızartması", "gramaj": "150 g", "enerji": ""},
                {"ad": "Peynirli Börek", "gramaj": "60 g", "enerji": ""},
                {"ad": "Beyaz Peynir", "gramaj": "40 g", "enerji": ""},
                {"ad": "*Siyah/Yeşil Zeytin", "gramaj": "30 g", "enerji": ""},
                {"ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"ad": "500 ml Su", "gramaj": "", "enerji": ""},
                {"ad": "**Çay/Bitki Çayı", "gramaj": "", "enerji": ""}
            ]
        },
        "30.11.2026": {
            "tarih": "30.11.2026",
            "gun": "Pazartesi",
            "ogun": "Sabah Kahvaltısı",
            "yemekler": ["Haşlanmış Yumurta", "Patates Salatası", "Sade Poğaça", "Kaşar Peynir", "*Siyah/Yeşil Zeytin"],
            "ogeler": [
                {"ad": "Haşlanmış Yumurta", "gramaj": "1 adet L boy", "enerji": ""},
                {"ad": "Patates Salatası", "gramaj": "150 g", "enerji": ""},
                {"ad": "Sade Poğaça", "gramaj": "1 adet", "enerji": ""},
                {"ad": "Kaşar Peynir", "gramaj": "40 g", "enerji": ""},
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
    "baslik": "KASIM AYI AKŞAM YEMEĞİ MENÜ TASLAĞI",
    "ay": "Kasım 2026",
    "notlar": [
        "Not: (08.11-20.11) Tarihlerinde Ahmet Kabaklı, (02.11-17.11) Sare Ana, Harput, İzzetpaşa (11.11-27.11) Ömer Bilginoğlu, Fethi Sekin, Fırat, yurtlarımızda (Mercimek çorba, Lahmacun, Mevsim Salata, Ayran) menüsü verilecektir."
    ],
    "imza": {
        "isim": "Abdulsamet EREN",
        "unvan": "Gençlik ve Spor İl Müdürü"
    },
    "gunler": {
        "01.11.2026": {
            "tarih": "01.11.2026",
            "gun": "Pazar",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorba / Şehriye Çorba",
                "Tavuk Kavurma / İmam Bayıldı / Çiftlik Kebabı",
                "Soslu Makarna",
                "Haydari"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorba / Şehriye Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Kavurma / İmam Bayıldı / Çiftlik Kebabı", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Soslu Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Haydari", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "02.11.2026": {
            "tarih": "02.11.2026",
            "gun": "Pazartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorba / Düğün Çorba",
                "Etli Kuru Fasülye / Mevsim Soslu Karışık Kızartma / Tavuk Çöp Şiş",
                "Şehriyeli Bulgur Pilavı",
                "Baklava (Cevizli)"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorba / Düğün Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Etli Kuru Fasülye / Mevsim Soslu Karışık Kızartma / Tavuk Çöp Şiş", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Şehriyeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Baklava (Cevizli)", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "03.11.2026": {
            "tarih": "03.11.2026",
            "gun": "Salı",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Domates Çorba / Yayla Çorba",
                "Tavuk Döner(%90) / Karışık Sebze Graten",
                "Sade Pirinç Pilav",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Domates Çorba / Yayla Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Döner(%90) / Karışık Sebze Graten", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sade Pirinç Pilav", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "04.11.2026": {
            "tarih": "04.11.2026",
            "gun": "Çarşamba",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin Çorba / Tutmaç Çorba",
                "Hamburger Köfte+Patates / Tavuk Burger / Yoğurtlu Karnabahar",
                "Makarna Salatası",
                "Sütlaç"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin Çorba / Tutmaç Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Hamburger Köfte+Patates / Tavuk Burger / Yoğurtlu Karnabahar", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Makarna Salatası", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Sütlaç", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "05.11.2026": {
            "tarih": "05.11.2026",
            "gun": "Perşembe",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Terbiyeli Sebze Çorba / Domates Çorba",
                "Fırında Sebzeli Tavuk Izgara / Mevsim Türlü / Etli Dolma",
                "Sebzeli Bulgur Pilavı",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Terbiyeli Sebze Çorba / Domates Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Fırında Sebzeli Tavuk Izgara / Mevsim Türlü / Etli Dolma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sebzeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "06.11.2026": {
            "tarih": "06.11.2026",
            "gun": "Cuma",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorba / Ayran Aşı Çorba",
                "Orman Kebap / İspanak Yemeği / Şinitzel",
                "Nohutlu Pirinç Pilavı",
                "Cacık"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorba / Ayran Aşı Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Orman Kebap / İspanak Yemeği / Şinitzel", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Nohutlu Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Cacık", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "07.11.2026": {
            "tarih": "07.11.2026",
            "gun": "Cumartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Şehriye Çorba / Yayla Çorba",
                "Tavuk Fajita / Yoğurtlu Mantı / Kilis Tava",
                "Fırın Makarna",
                "Browni"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Şehriye Çorba / Yayla Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Fajita / Yoğurtlu Mantı / Kilis Tava", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Fırın Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Browni", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "08.11.2026": {
            "tarih": "08.11.2026",
            "gun": "Pazar",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorba / Mısır Çorba",
                "Çiftlik Köfte / Nugget / Taze Fasülye",
                "Şehriyeli Bulgur Pilavı",
                "Havuç Tarator"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorba / Mısır Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Çiftlik Köfte / Nugget / Taze Fasülye", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Şehriyeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Havuç Tarator", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "09.11.2026": {
            "tarih": "09.11.2026",
            "gun": "Pazartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorba / Yayla Çorba",
                "Kavurma / Bezelye Yemeği / Tavuk Çöp Şiş",
                "Sade Pirinç Pilav",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorba / Yayla Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Kavurma / Bezelye Yemeği / Tavuk Çöp Şiş", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sade Pirinç Pilav", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "10.11.2026": {
            "tarih": "10.11.2026",
            "gun": "Salı",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Terbiyeli Sebze Çorba / Şehriye Çorba",
                "Tavuk Tantuni / Taze Fasülye / Karnıyarık",
                "Soslu Makarna",
                "Haydari"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Terbiyeli Sebze Çorba / Şehriye Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Tantuni / Taze Fasülye / Karnıyarık", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Soslu Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Haydari", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "11.11.2026": {
            "tarih": "11.11.2026",
            "gun": "Çarşamba",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorba / Domates Çorba",
                "Etli Kuru Fasülye / Mevsim Türlü / Nugget",
                "Şehriyeli Bulgur Pilavı",
                "Yoğurt",
                "Şekerpare"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorba / Domates Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Etli Kuru Fasülye / Mevsim Türlü / Nugget", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Şehriyeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Yoğurt", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Şekerpare", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "12.11.2026": {
            "tarih": "12.11.2026",
            "gun": "Perşembe",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorba / Şehriye Çorba",
                "Fırında Tavuk Biftek / Mücver / Etli Dolma",
                "Gökkuşağı Pirinç Pilav",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorba / Şehriye Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Fırında Tavuk Biftek / Mücver / Etli Dolma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Gökkuşağı Pirinç Pilav", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "13.11.2026": {
            "tarih": "13.11.2026",
            "gun": "Cuma",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin Çorba / Sebze Çorba",
                "Rosto Köfte / Sulu Patates / Şinitzel",
                "Soslu Makarna",
                "Ayran veya Meyve Suyu"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin Çorba / Sebze Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Rosto Köfte / Sulu Patates / Şinitzel", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Soslu Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Ayran veya Meyve Suyu", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "14.11.2026": {
            "tarih": "14.11.2026",
            "gun": "Cumartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Dövme Çorba / Süzme Çorba",
                "Çıtır Tavuk / Ispanak Kavurma / Güveç",
                "Sebzeli Bulgur Pilavı",
                "Sütlaç"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Dövme Çorba / Süzme Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Çıtır Tavuk / Ispanak Kavurma / Güveç", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sebzeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Sütlaç", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "15.11.2026": {
            "tarih": "15.11.2026",
            "gun": "Pazar",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Yayla Çorba / Şehriye Çorba",
                "Kuşbaşılı Patlıcan Kebap / Tavuk Kavurma / Bezelye Yemeği",
                "Şehriyeli Pirinç Pilavı",
                "Havuç Tarator"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Yayla Çorba / Şehriye Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Kuşbaşılı Patlıcan Kebap / Tavuk Kavurma / Bezelye Yemeği", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Şehriyeli Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Havuç Tarator", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "16.11.2026": {
            "tarih": "16.11.2026",
            "gun": "Pazartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorba / Düğün Çorba",
                "Soslu Fırında Tavuk / Mevsim Türlü / Etli Nohutlu Mantı",
                "Soslu Makarna",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorba / Düğün Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Soslu Fırında Tavuk / Mevsim Türlü / Etli Nohutlu Mantı", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Soslu Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "17.11.2026": {
            "tarih": "17.11.2026",
            "gun": "Salı",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin Çorba / Tutmaç Çorba",
                "Fırında Dizme Köfte / Çıtır Tavuk+Patates Kızartması / Mücver",
                "Sade Bulgur Pilavı",
                "Revani"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin Çorba / Tutmaç Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Fırında Dizme Köfte / Çıtır Tavuk+Patates Kızartması / Mücver", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sade Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Revani", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "18.11.2026": {
            "tarih": "18.11.2026",
            "gun": "Çarşamba",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorba",
                "İstavrit (Balık) / Soslu Karışık Kızartma",
                "Mevsim Salata",
                "Helva"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "İstavrit (Balık) / Soslu Karışık Kızartma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Helva", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "19.11.2026": {
            "tarih": "19.11.2026",
            "gun": "Perşembe",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin Çorba / Mısır Çorba",
                "Ekmek Arası Köfte / Tavuk Sote / Yoğurtlu Mantı",
                "Şehriyeli Pirinç Pilavı",
                "Ayran"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin Çorba / Mısır Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Ekmek Arası Köfte / Tavuk Sote / Yoğurtlu Mantı", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Şehriyeli Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Ayran", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "20.11.2026": {
            "tarih": "20.11.2026",
            "gun": "Cuma",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Süzme Çorba / Yayla Çorba",
                "Etli Kuru Fasülye / Etli Dolma / Tavuk Çöp Şiş",
                "Erişte Pilav",
                "Baklava (Cevizli)"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Süzme Çorba / Yayla Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Etli Kuru Fasülye / Etli Dolma / Tavuk Çöp Şiş", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Erişte Pilav", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Baklava (Cevizli)", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "21.11.2026": {
            "tarih": "21.11.2026",
            "gun": "Cumartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Dövme Çorba / Ayran Aşı Çorba",
                "Karnıyarık / Tavuk Tantuni / Pırasa",
                "Sade Pirinç Pilavı",
                "Cacık"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Dövme Çorba / Ayran Aşı Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Karnıyarık / Tavuk Tantuni / Pırasa", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sade Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Cacık", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "22.11.2026": {
            "tarih": "22.11.2026",
            "gun": "Pazar",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Sebze Çorba / Mercimek Çorba",
                "Patlıcan Parmak Kebabı / Yoğurtlu Mantı / Tavuk Baget Kızartma",
                "Sebzeli Bulgur Pilavı",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Sebze Çorba / Mercimek Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Patlıcan Parmak Kebabı / Yoğurtlu Mantı / Tavuk Baget Kızartma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sebzeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "23.11.2026": {
            "tarih": "23.11.2026",
            "gun": "Pazartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Ezogelin Çorba / Tutmaç Çorba",
                "Tavuk Döner(%90) / Karışık Sebze Grateni",
                "Sade Pirinç Pilav",
                "Islak Kek"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Ezogelin Çorba / Tutmaç Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tavuk Döner(%90) / Karışık Sebze Grateni", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sade Pirinç Pilav", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Islak Kek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "24.11.2026": {
            "tarih": "24.11.2026",
            "gun": "Salı",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorba / Domates Çorba",
                "Çiftlik Köfte / Tavuk Kavurma / Soslu Karışık Kızartma",
                "Makarna Salatası",
                "Ayran veya Meyve Suyu"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorba / Domates Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Çiftlik Köfte / Tavuk Kavurma / Soslu Karışık Kızartma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Makarna Salatası", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Ayran veya Meyve Suyu", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "25.11.2026": {
            "tarih": "25.11.2026",
            "gun": "Çarşamba",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorba / Ayran Aşı Çorba",
                "Tas Kebabı / Şinitzel / İmam Bayıldı",
                "Şehriyeli Bulgur Pilavı",
                "Haydari"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorba / Ayran Aşı Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Tas Kebabı / Şinitzel / İmam Bayıldı", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Şehriyeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Haydari", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "26.11.2026": {
            "tarih": "26.11.2026",
            "gun": "Perşembe",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Terbiyeli Sebze Çorba / Şehriye Çorba",
                "Fırın Tavuk Baget / Sebze Graten / Etli Taze Fasülye",
                "Soslu Makarna",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Terbiyeli Sebze Çorba / Şehriye Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Fırın Tavuk Baget / Sebze Graten / Etli Taze Fasülye", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Soslu Makarna", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "27.11.2026": {
            "tarih": "27.11.2026",
            "gun": "Cuma",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorba / Yayla Çorba",
                "Etli Nohut / Yoğurtlu Mantı / Tavuk Fajita",
                "Şehriyeli Pirinç Pilavı",
                "Mercimek Köfte",
                "Puding"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorba / Yayla Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Etli Nohut / Yoğurtlu Mantı / Tavuk Fajita", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Şehriyeli Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mercimek Köfte", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Puding", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "28.11.2026": {
            "tarih": "28.11.2026",
            "gun": "Cumartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Dövme Çorba / Domates Çorba",
                "Çiftlik Kebabı / Nugget / Dolma",
                "Sebzeli Bulgur Pilavı",
                "Mevsim Salata"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Dövme Çorba / Domates Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Çiftlik Kebabı / Nugget / Dolma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Sebzeli Bulgur Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "29.11.2026": {
            "tarih": "29.11.2026",
            "gun": "Pazar",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Mercimek Çorba",
                "Somon (Balık) / Soslu Karışık Kızartma",
                "Mevsim Salata",
                "Helva"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Mercimek Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Somon (Balık) / Soslu Karışık Kızartma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Mevsim Salata", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Helva", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "Çeyrek Ekmek", "gramaj": "", "enerji": ""},
                {"kategori": "Ek", "ad": "500 ml Su", "gramaj": "", "enerji": ""}
            ]
        },
        "30.11.2026": {
            "tarih": "30.11.2026",
            "gun": "Pazartesi",
            "ogun": "Akşam Yemeği",
            "yemekler": [
                "Tarhana Çorba / Mısır Çorba",
                "Hamburger Köfte+Patates / Tavuk Burger / Ispanak Kavurma",
                "Şehriyeli Pirinç Pilavı",
                "Tulumba"
            ],
            "ogeler": [
                {"kategori": "1. Yemek Çeşitleri", "ad": "Tarhana Çorba / Mısır Çorba", "gramaj": "", "enerji": ""},
                {"kategori": "2. Yemek Çeşitleri", "ad": "Hamburger Köfte+Patates / Tavuk Burger / Ispanak Kavurma", "gramaj": "", "enerji": ""},
                {"kategori": "3. Yemek Çeşitleri", "ad": "Şehriyeli Pirinç Pilavı", "gramaj": "", "enerji": ""},
                {"kategori": "4. Yemek Çeşitleri", "ad": "Tulumba", "gramaj": "", "enerji": ""},
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

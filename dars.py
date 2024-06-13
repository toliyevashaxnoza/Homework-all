ismlar = ['zilola', 'shahnoza', ' gullola']
duganam = "assalomu aleykum, " + ismlar[0].title() + "!"
print(duganam)
duganam = "Yaxshimjsan, " + ismlar[1].title() + "!"
print(duganam)
duganam = "nima gaplar, " + ismlar[2].title() + "!"
print(duganam)


davlatlar= {
    'Xorazim':'Toshkent',
    'Turkiya':'Anqara',
    'Avgoniston':'Qobul',
    'Qozogiston':'Nur-Sulton',
    'Pokiston':'Islomobod',
    'Hindiston':'Dehli',
    'Qirgiziston':'Bishkek',
    'Tojikiston': 'Dushanbe'
}
print('Dunyo davlatlari:')
for davlat in sorted(davlatlar):
    print(davlat.title())

print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

    davlatlar = {
        "o'zbekiston": 'toshkent',
        'hindiston': 'dehli',
        'rossiya': 'moskva',
        'tojikiston': 'dushanbe',
        "qirg'iziston": 'bishkek',
        'pokiston': 'islomobod',
        'turkiya': 'anqara',
        'qozogiston': 'nur-sulton',
        'italiya': 'rim'
    }

    mamlakat = input('Xoxlagan davlatni nomini kiriting.Poytaxtini chiqarib beramiz?:').lower()
    poytaxt = davlatlar.get(mamlakat)
    if poytaxt == None:
        print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
    else:
        print(f"{mamlakat.title()}ning po

        inolar = {
            'Murodjon': ['taxi1', 'shum bola', 'Qorqinchli'],
            'Soburjon': ['ujas', 'hind kino', 'sarguzasht'],
            'Shaxnoza': ['zamonaviy', 'ibratli', 'foydali']
        }

        for ism, kinolar in kinolar.items():
            print(f"\n{ism.title()}ning sevimli kinolari:")
        for kino in kinolar:
            print(kino)

        davlatlar = {
            "o'zbekiston": {'poytaxt': "toshkent",
                            'maydon': 448978,
                            'aholi': 33_000_000,
                            'pul birligi': "so'm"
                            },
            "rossiya": {'poytaxt': "moskva",
                        'maydon': 14_098_246,
                        'aholi': 144_000_000,
                        'pul birligi': "rubl"
                        },
            "aqsh": {'poytaxt': "vashington",
                     'maydon': 8_631_418,
                     'aholi': 316_000_000,
                     'pul birligi': "dollar"},
            "Hindiston": {'poytaxt': "Dehli",
                          'maydon': 329750,
                          'aholi': 1_413_179_280,
                          'pul birligi': "rupiy"}
        }

        for davlat, info in davlatlar.items():
            if
        davlat.lower() == 'aqsh':
        davlat = davlat.upper()
        else:
        davlat = davlat.capitalize()
        print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
              f"\nHududi: {info['maydon']} kv.km"
              f"\nAholisi: {info['aholi']}"
              f"\nPul birligi: {info['pul birligi']}")

        davlatlar = {
            "o'zbekiston": {'poytaxt': "toshkent",
                            'maydon': 448978,
                            'aholi': 33_000_000,
                            'pul birligi': "so'm"
                            },
            "rossiya": {'poytaxt': "moskva",
                        'maydon': 14_098_246,
                        'aholi': 144_000_000,
                        'pul birligi': "rubl"
                        },
            "aqsh": {'poytaxt': "vashington",
                     'maydon': 8_631_418,
                     'aholi': 316_000_000,
                     'pul birligi': "dollar"},
            "Hindiston": {'poytaxt': "Dehli",
                          'maydon': 329750,
                          'aholi': 1_413_179_280,
                          'pul birligi': "rupiy"}
        }

        davlat = input('Davlat nomini kiriting: ').lower()
        if davlat in davlatlar:
            info = davlatlar[davlat]
        print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
              f"\nHududi: {info['maydon']} kv.km"
              f"\nAholisi: {info['aholi']}"
              f"\nPul birligi: {info['pul birligi']}")
        else:
        print("Bizda bu davlat haqida ma'lumot mavjud emas")
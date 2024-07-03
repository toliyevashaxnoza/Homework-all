def kopaytma(*sonlar):
    if len(sonlar) == 0:
        return 0
    kopaytma_natija = 1
    for son in sonlar:
        kopaytma_natija *= son
    return kopaytma_natija

sonlar1 = 2, 3, 4
sonlar2 = 5, 6, 7, 8

print("Birinchi kopaytma natijasi:", kopaytma(*sonlar1))  # 2 * 3 * 4 = 24
print("Ikkinchi kopaytma natijasi:", kopaytma(*sonlar2))


def talaba_malumotlari(ism, familiya, **malumotlar):
    talaba = {
        'ism': ism,
        'familiya': familiya
    }
    talaba.update(malumotlar)
    return talaba

talaba1 = talaba_malumotlari('Ali', 'Valiyev', yosh=20, universitet='Oxford')
talaba2 = talaba_malumotlari('Diana', 'Saidova', yosh=22, universitet='Harvard', yoqtirgan_fani='Biologiya')

print("Talaba 1 ma'lumotlari:", talaba1)
print("Talaba 2 ma'lumotlari:", talaba2)
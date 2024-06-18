#                                     *args USULI
def summa(*sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
        return yigindi
print(summa(10,12,6,-5))
#
def summa (*sonlar):
    return sum (sonlar)
print(summa(4,5,6,7))
#
#
def summa(x,y,*sonlar):
    return x+y+sum(sonlar)

print(summa(16,22,55,66,112,115,448))

#                                                **kwargas USULI

def avto_info(kompaniya,madel,**malumotlar):
    malumotlar['kompaniya']=kompaniya
    malumotlar['model'] = madel
    return malumotlar

avto1 = avto_info("Gm","malibu",rang='qora',yil=2018,narh=400000000)
avto2 = avto_info("Kia","K5",rang='qiil',narh=35000)


print(avto1)
print(avto2)


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto


def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting",end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")
        #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
        #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
    return avtolar


def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")
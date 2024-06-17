#1. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib,
# lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni
# kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)



def foydalanuvchi_mijoz(ism, familiya, tyil, tjoy, email='',tel=None):
    foydalanuvchi_mijoz= {'ism':ism,
             'familiya':familiya,
             'tyil':tyil,
             'yoshi':2024-tyil,
             'tjoy':tjoy,
             'email':email,
             'telefon':tel}
    return foydalanuvchi_mijoz


print("Mijoz haqida ma'lumotlarni kiriting.")


#2. Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.


mijozlar =[]
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(foydalanuvchi_mijoz(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob!='ha':
        break

print("Mijozlar:")
for foydalanuvchi_mijoz in mijozlar:
    print(f"{foydalanuvchi_mijoz['ism'].title()} {foydalanuvchi_mijoz['familiya'].title()},"
          f"{foydalanuvchi_mijoz['yoshi']} yoshda, telefoni: {foydalanuvchi_mijoz['telefon']}")

#3.Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing.

def kattasi(x,y,z):
    mx  = x
    if y>=mx:
        mx = y
    if z>=mx:
        mx = z
    return mx
print(kattasi(20,30,-5))



#4.Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini
# lug'at ko'rinishida qaytaruvchi funksiya yozing

# def aylana_r(radius,p=3.14):
#     aylana = {"radius":radius,
#               "diametr":2*radius,
#               "perimetr":2*radius*p,
#               "yuza":p*radius**2}
#     return aylana
#
# print(aylana_r(15))


#5.Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def tub_sonlar_t(mn, mx):
    tub_sonlar = []
    for n in range(mn, mx + 1):
        tub = True
        if (n == 1):
            tub = False
        elif (n == 2):
            tub = True
        else:
            for x in range(2, n):
                if (n % x == 0):
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar


print(tub_sonlar_t(1, 100))

#6.Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.
# Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi.
# Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(100))
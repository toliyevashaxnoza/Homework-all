#1. Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def numbers(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(numbers(8,9,10))

#2.Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda
# istalgancha berilishi mumkin bo'lsin.


def talaba_t(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_t('shaxnoza','toliyeva',tyil=2006,fakultet='IT',yonalish='AT')
print(talaba)

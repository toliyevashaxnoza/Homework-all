#1. savat =[]
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
    if javob != 'ha':
        break
#2. mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
    mahsulotlar[mahsulot] = narh
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != 'ha':
        break

# 3. buyurtmalar = ['olma', 'non', 'banan', 'limon']
mahsulotlar = {'olma': 20000,
                       'banan': 25000,
                       'olma': 18000,
                       'non': 2200}
while buyurtmalar:
            buyurtma = buyurtmalar.pop()
            if buyurtma in mahsulotlar.keys():
                narh = mahsulotlar[buyurtma]
                print(f"{buyurtma.title()} - {narh} so'm")
            else:
                print(f"Bizda {buyurtma} yo'q")
class User:
    """Faydalanuvchi user  klass yaratamiz"""

    def __init__(self, ism, familiya, email,nomer,adress):
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.nomer = nomer
        self.adress = adress

    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.email} yilda tu'gilganman {self.nomer}, {self.adress}")
nomzot1=User("Usmon","Abdullayev","abdullayevusmon0303@gmail.com", 930805565 ,"Gaybu")
print(f"Ismi:{nomzot1.ism} familiya:{nomzot1.familiya} elektron pochta:{nomzot1.email} Raqam:{nomzot1.nomer} {nomzot1.adress}da tugilgan")

###################################################################################################
class User:
    """Faydalanuvchi user  klass yaratamiz"""

    def __init__(self, ism, familiya, email,adress):
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.adress = adress

    def get_info(self):
       return f"{self.ism} {self.familiya}. {self.email} {self.adress} "\

nomzot1 = User('Ismi:'"Usmon", "Abdullayev", 'email:'"abdullayevusmon0303@gmail.com" ,'Manzil:'"Urganch"'da tugilgan')
print(nomzot1.get_info())

#######################################################################################################
class User:
    """Foydalanuvchi user klass yaratamiz"""
    def __init__(self,ism,familiya,tyil,email,adress):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.email=email
        self.adress=adress

    def get_name(self):
        """Foydalanuvchini ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Foydalanuvchini familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Foydalanuvchini ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def tanishtr(self):
        print(f"Ismim {self.ism} {self.familiya} {self.tyil} yilda tugilganman  {self.adress}da tugilgan email:{self.email}")

    def get_age(self,yil):
        """Foydalanuvchini yoshini qaytaradi"""
        return yil-self.tyil

    def get_email(self):
        """Foydalanuvchini emailni qaytyaradi"""
        return self.email

    def get_adress(self):
        return self.adress

mzot1=User("Usmon","Abdullayev",2005,"usmonabdullayev@gmail.com","Xorazm")
print(nomzot1.tanishtr())
print(nomzot1.get_lastname())
print(nomzot1.get_name())
print(nomzot1.get_fullname())
int(nomzot1.get_age(2024))
print(nomzot1.get_email())
print(nomzot1.get_adress())


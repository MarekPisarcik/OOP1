
# Vytvorenie triedy a atributov:
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand # nastavene hodnoty v konstruktore
        self.model = model
        self.year = year

# Vytvorenie metody car_info()
    def car_info(self):
        return f"Znacka: {self.brand}, Model: {self.model}, Rok: {self.year} "

# Vytvorenie objektov (instancii) triedy
japonske_auto = Car("Mazda", "2", "2009")
francuzke_auto = Car("Renault", "Megane", "2014")
talianske_auto = Car("Fiat", "Punto", "2025")

# Vypisanie atributov objektov
#print(japonske_auto.__dict__) # pouzity prikaz __dict__, ktory vypise vsetko

# Volanie metody car_inf() v objektoch
print(talianske_auto.car_info(), japonske_auto.car_info())
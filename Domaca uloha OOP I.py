


# 1.1 Vytvorenie triedy pre balik v dorucovacej sluzbe
class Package:
    def __init__(self, sender, recipient, weight, status):
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
        self.status = status
# 1.2 Metody v triede
    def __str__(self):
        return f"Balik pre: {self.sender}, Od: {self.recipient}, Vaha: {self.weight}, Stav: {self.status}"
# 1.3 Getter
    @property
    def delivered(self):
        return self.status == "Doruceny"
    # Setter
    @delivered.setter
    def delivered(self, nova_hodnota):
        if nova_hodnota:
            self.status = "Doruceny"
        else:
            self.status = "Na ceste"
balik1 = Package("School", "Marek", "0.5", "Na ceste")
balik2 = Package("Work", "Radovit", "2", "Doruceny")

print(balik1.__str__())
print(balik2.__str__())

balik1.delivered = False
print(balik1.delivered)
print(balik1.status)

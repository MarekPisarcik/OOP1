


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

balik1 = Package("School", "Marek", "0.5", "Na ceste")
balik2 = Package("Work", "Radovit", "2", "Doruceny")

print(balik1.__str__())
print(balik2.__str__())



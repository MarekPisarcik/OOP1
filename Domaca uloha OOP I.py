


# 1.1 Vytvorenie triedy pre balik v dorucovacej sluzbe
class Package:
    def __init__(self, sender, recipient, weight, status):
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
        self.status = status

balik1 = Package("School", "Marek", "0.5", "Na ceste")
balik2 = Package("Work", "Radovit", "2", "Doruceny")

print(balik1.__dict__)


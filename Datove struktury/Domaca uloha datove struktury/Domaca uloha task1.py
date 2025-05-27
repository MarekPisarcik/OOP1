from symtable import Class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        novy_uzol = Node(data)

        if not self.head:
            self.head = novy_uzol

        else:
            aktualny = self.head
            while aktualny.next:
                aktualny = aktualny.next
            aktualny.next = novy_uzol

    def vypis(self):
        aktualny = self.head
        while aktualny:
            print(aktualny.data, end="--->")
            aktualny = aktualny.next
        print("koniec zoznamu linked list")

def main():
    ll = linked_list()

    for i in range(10):
        number = int(input(f"Zadaj cislo {i + 1}: "))
        ll.append(number)

    print("\n Tvoj linked list je:")
    ll.vypis()

main()
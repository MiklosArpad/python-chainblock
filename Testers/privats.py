
# itt hozható létre az Encapsulation - azaz az egységbe zárás

class Szemely:
    def __init__(self, nev):
        self.__nev = nev

    def get_nev(self):
        return self.__nev

sz = Szemely("Valaki")
print(sz.get_nev())
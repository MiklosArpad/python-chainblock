
from datetime import datetime
import hashlib
from transaction import Transaction



class Block:
    def __init__(self, date, transaction, prev_hash=None):
        self.__date = date
        self.__transaction = transaction
        self.__prev_hash = prev_hash
        self.__hash = self.calculate_hash()

    def calculate_hash(self):
        date = str(self.__date).encode()
        transaction = str(self.__transaction).encode()
        prev_hash = self.__prev_hash.hexdigest().encode() if self.__prev_hash else str(None).encode()
                                # ez a python turnary if kondicio

        return hashlib.sha256(date + transaction + prev_hash)

    def get_hash(self):
        return self.__hash

    def get_prev_hash(self):
        return self.__prev_hash

    def __str__(self):     # ez egy magic metods és még double under (dunder methods
        if self.__prev_hash is None:
            return f"Block: {self.get_hash().hexdigest()}; Transaction: {self.__transaction}; Previous hash: {None}"
        return f"Block: {self.get_hash().hexdigest()}; Transaction: {self.__transaction}; Previous hash: {self.get_prev_hash().hexdigest()}"

if __name__ == "__main__":

    print(datetime.now())
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))   # string format ebben nincs mili sec


    #b1 = Block(datetime.now(), "Valami nagyon fals szöveget ide!") # ez a Genesis Hash
    #b2 = Block(datetime.now(), "Valami mégnagyobb fals szöveget ide!", b1.get_hash())
    #b3 = Block(datetime.now(), "Valami mégnagyobb fals szöveget ide!", b2.get_hash())

    # EZ A GENESIS BLOCK
    b1 = Block(datetime.now(), Transaction("Jozsi", "Bela", 100))
    b2 = Block(datetime.now(), Transaction("Feri", "Teri", 25), b1.get_hash())
    b3 = Block(datetime.now(), Transaction("Pali", "Vali", 85), b2.get_hash())

    print(b1)
    print(b2)
    print(b3)
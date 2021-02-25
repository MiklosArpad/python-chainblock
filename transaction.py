
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.__sender = sender
        self.__receiver = receiver
        self.__amount = amount


    def __str__(self):
        return f"{self.__sender} sent {self.__amount} coins to {self.__receiver}."

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def get_amount(self):
        return self.__amount

if __name__ == "__main__":
    tr1 = Transaction("Jozsi", "Bela", 100)

    print(tr1)


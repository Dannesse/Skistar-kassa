class rent:
    def __init__(self, thing, brand, size, amount, prize,):
        self.thing = thing
        self.brand = brand
        self.size = size
        self.amount = amount
        self.prize = prize


    def get_name(self):
        return self.thing

    def get_answer(self):
        return self.brand

    def get_choices(self):
        return self.size

    def get_name(self):
        return self.amount

    def get_answer(self):
        return self.prize

    def choice(self):
     pass

#priset varierar beroende på hyr länge de ska hyr

def load_hyr():
    with open("Hyr_sak.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            selection = line.split("/")
def main():
    pass

if __name__ == "__main__":
    pass


main()
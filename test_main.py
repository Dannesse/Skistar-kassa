class Rent:
    def __init__(self, thing, brand, size, amount, price):
        self.thing = thing
        self.brand = brand
        self.size = size
        self.amount = amount
        self.price = price

    def get_all_attributes(self):
        return self.thing, self.brand, self.size, self.amount, self.price

    def get_brand(self):
        return self.brand

    def get_size(self):
        return self.size

    def get_amount(self):
        return self.amount

    def get_price(self):
        return self.price

    def get_thing(self):
        return self.thing

    def __str__(self):
        return f"{self.brand}. Storlek {self.size} m/rum "

def save_amount(characters : list()):
    saved_amounts = []
    for character in characters:
        thing, brand, size, amount, price = character.get_all_attributes()
        save_string = f"{thing}/{brand}/{size}/{amount}/{price}\n"
        saved_amounts.append(save_string)
        
    with open("Skistar-kassa\ent_ski.txt", "w", encoding="utf8") as f:
        for alt in saved_amounts:
            f.write(alt)
        print(f"Antelt i lagret har ändras.")

def load_alternativs():
    with open("Skistar-kassa\ent_ski.txt", "r", encoding="utf8") as f:
        loan = []
        for line in f.readlines():
            attributes = line.split("/")
            this_alt = Rent(attributes[0], 
                                  str(attributes[1]),
                                  float(attributes[2]),
                                  int(attributes[3]),
                                  int(attributes[4]))
            loan.append(this_alt)
    f.close()
    return loan

def rent_stuff(alternativ,):
    price_amout = 0 
    price_card = 0
    running1 = True
    running = True
    running2 = True
            
    if alternativ.lower() == "b":
        time_card = int(input("Okej, hur länge vill du hyra liftkortet i dagar? "))
        card_amout = int(input ("Hur många liftkort vill du hyra? "))
        price_card = time_card * card_amout *180
        print("")
        choice_after_card = input(f"Just nu är kostnaden på {price_card} kr. Skriv a för att hyra annat. Skriv b för att betala ")
        if choice_after_card == "b":
            choice_after_rent = "b"

    elif alternativ.lower() == "a" or choice_after_card == "a":
        while running1:
            choice_thing = input("vad vill du hyra\nBoende\nSkidor? ")
            if choice_thing.lower() == "b":
                running1 = False
            elif choice_thing.lower() == "s":
                running1 = False
            else:
                print("Something went wrong...\nTry again..")
        loan1 = load_alternativs()
        for i in loan1:
            if i.get_thing() == choice_thing:
                print(f"{i}")
        print("")
        while running:
            print("Nedan är det en lista på skid märken som du kan hyra och vilka storlekar det finns på märket.")
            for i in loan1:
                print(i.get_brand())
            choice_brand = input(f"Välj ett {choice_thing} märke/typ.")
            for i in loan1:
                if choice_brand.lower() == i.get_brand().lower():
                    print(f"Du har valt {i}.\n")
                    running = False
        print("")                
        while running2:
            choice_size = float(input("Vilken storlek vill du ha av fån alternativerna ovan: "))
            for i in loan1:
                if choice_size == i.get_size():
                    running2 = False
        print("")
    check_amount(choice_brand, choice_size, price_card)

def check_amount(choice_brand, choice_size, price_card):
    loan = load_alternativs()
    new_list = []
    for i in loan:
        if i.get_size() == choice_size and i.get_brand().lower() == choice_brand.lower() and i.get_amount()>=1:
            new_amount = i.get_amount() - 1
            print(f"Du har valt {i}")
            print(f"Det fins {new_amount} kvar i lagret")
            thing, brand, size, amount, price = i.get_all_attributes()
            old_string = f"{thing}/{brand}/{size}/{amount}/{price}\n"
            new_string = f"{thing}/{brand}/{size}/{new_amount}/{price}\n"
            with open("Skistar-kassa\ent_ski.txt", "r+", encoding="utf8") as f:
                loan_list = f.readlines()
                for line_str in loan_list:
                    if old_string == line_str:
                        new_list.append(new_string)
                    else:
                        new_list.append(line_str)
                f.close()
            with open("Skistar-kassa\ent_ski.txt", "w", encoding="utf8") as f:
                for _ in new_list:
                    f.write(_)
                f.close()

            print("")
            loan_days = int(input("Hur många dagar ska du hyra utrustingen? "))
            price_amout = loan_days * i.get_price()
            print(f"Då blir kostanden {price_amout} kr ")
            choice_after_rent = input(f"Kostnaden för hyrandet blir {price_amout} kr. Skriv b för att betala ")
    if i.get_size() == choice_size and i.get_brand() == choice_brand and i.get_amount()<1:
        print(f"Tyvärr är alla {choice_brand} i längden {choice_size} redan uthyrda")
    
    if choice_after_rent == "b" :
        total_price = price_amout + price_card
        print(f"{total_price}") 

def main():
    print("Hej och välkommen till skistars kassa.")
    alternativ = input ("Vad vill du göra? Du kan antagligen a) Hyra utrustning och/eller boende b) köpa liftkort eller båda\nSkirv här: ")
    rent_stuff(alternativ)


if __name__ == "__main__":
    main()
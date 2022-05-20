
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
        return f"{self.brand}\nStorlek {self.size} m/rum\n "

def load_alternitivs():
    """Open the file with all the options""" 
    
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

def rent_stuff(alternitiv,):
    """What the user sees and alternatives for what they want to do.
    Plus functions that remove what the user rents from the "werehouse"/file and add what the user returns
   
    Args:
        price_amount (int): The price of what the user rents. If the user does not rent then the price is 0.
        price_card (int): The price for the lift pass. If the user does not rent lift pass then the price is 0.
        Running, running1, running2, running3: For while-loops. The loop/variable is true until it is named false.
        Time_card (int): How long the user is going to rent the lift pass
        time_amount (int): How many lift cards the user rents
        price_card  (int): The total price for the lift pass
        choice_after_card (str): The user choice to rent more or pay
        choice_after_rent (str): To go to payment after the user has rented skis or accommodation.
        loan1 (list): Go to function load_alternitivs to load and open the file with different alternatives.
        choice_brand (str): User choose the brand they want
        choice_thing (str): User chooses to rent skis or accommodations.
        choice_size (int): User chooses a size.
        new_amount (int): The new amount on what is rented.
        thing, brand, size, amount, price: Is the attributes from the Class rent.
        old_string (str): Is all old attributes and alternatives before the new amount changed.
        new_sting (str): Is the "new" updated file white new amounts.
        i (index)
        _ (index)
        loan_days (int): How long the user is going to rent
        price_amout (int): Total cost for only the rented items (skis/accommodation)
        total_price (int): Total price.
    """
    price_amout = 0 
    price_card = 0
    running1 = True
    running = True
    running2 = True
    running3 = True
            
    if alternitiv.lower() == "b": #lift pass
        time_card = int(input("Okej, hur länge vill du hyra liftkortet i dagar? "))
        card_amout = int(input ("\nHur många liftkort vill du hyra? "))
        price_card = time_card * card_amout *180
        print("")
        choice_after_card = input(f"\nJust nu är kostnaden på {price_card} kr. Skriv a för att hyra annat. Skriv b för att betala ")
        if choice_after_card == "b":
            choice_after_rent = "b"
            

    if alternitiv.lower() == "a" or choice_after_card == "a": #  Choose item, brand and size
        while running1:
            choice_thing = input("Vad vill du hyra?\nBoende\nSkidor?\nSvara här: ")
            if choice_thing.lower() == "boende":
                running1 = False
            elif choice_thing.lower() == "skidor":
                running1 = False
            else:
                print("\nNågot blev fel...\nFörsök igen..\n")
        loan1 = load_alternitivs()
        print("")
        while running:
            print("Nedan är det en lista på skid märken som du kan hyra och vilka storlekar det finns på märket.")
            print("-----------------------------------")
            for i in loan1:
                if i.get_thing() == choice_thing:
                    print(f"{i}")
            print("------------------------------------")
            choice_brand = input(f"Välj ett {choice_thing} märke/typ.")
            for i in loan1:
                if choice_brand.lower() == i.get_brand().lower():
                    print(f"Du har valt {i}.\n\n")
                    running = False
        print("")                

        while running2:
            print("------------------------------------")
            choice_size = float(input("Vilken storlek vill du ha av fån alternativerna ovan: "))
            for i in loan1:
                if choice_size == i.get_size():
                    running2 = False
        print("")


#Chek if the items are available
        #Changes and save the amount of items to the nrw amount in the file
        loan = load_alternitivs()
        new_list = []
        while running3:
            for i in loan:      
                if i.get_size() == choice_size and i.get_brand().lower() == choice_brand.lower() and i.get_amount()>=1:
                    new_amount = i.get_amount() - 1
                    print("---------------------------------")
                    print(f"Du har valt {i}")
                    print(f"Nu finns det {new_amount} kvar i lagret")
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
                    print("")
                    price_amout = loan_days * i.get_price()
                    print(f"Då blir kostanden {price_amout} kr ")
                    choice_after_rent = input(f"Kostnaden för hyrandet blir {price_amout} kr. Skriv b för att betala ")
                    running3 = False

            
                if i.get_size() == choice_size and i.get_brand().lower() == choice_brand.lower() and i.get_amount()<1:
                    
                    print(f"Tyvärr är alla {choice_brand} i längden {choice_size} redan uthyrda")
                    print(i)
                    choice_brand = input("Välj ett märke igen: ")
                    choice_size = float(input("Välj en annan storlek: "))
                    
    #The total price     
    if choice_after_rent == "b" :
        total_price = price_amout + price_card
        print(f"\nDen totala kostnanden blir {total_price} kr, tack") 

def return_loan(): #Returns items
    """The user reterns what they have rented.

    Args:
        loan2 (list): Go to function load_alternitivs to load and open the file with different alternatives.
        which_brand (str): User choose the brand thay want
        wich_size (int): User choose a size.
         


    """
    print("----------------------")
    loan2 = load_alternitivs()
    for i in loan2:
        print(i.get_brand())
    print("----------------------")    
    which_brand = input("\nVilket märke/typ av alternativerna ovan: ")
    print("----------------------")
    for i in loan2:
        if which_brand.lower() == i.get_brand().lower():
            print(f"\n{i}.\n")
    wich_size = float(input("Vilken storlek? "))

    new_list = []
    for i in loan2:     
        if i.get_size() == wich_size and i.get_brand().lower() == which_brand.lower():
            new_amount = i.get_amount() + 1
            print(f"\nDu har valt {i}")
            print(f"Tack, nu finns det {new_amount} kvar i lagret\n")
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
def main():
    print("Hej och välkommen till skistars kassa.")
    alternitiv1 = input("Vill du: \na) Hyra \nb) Lämna tillbaka\nSkriv här: ")
    if alternitiv1 == "a":
        alternitiv = input ("\nVad vill du göra? Du kan antagligen: \na) Hyra utrustning och/eller boende \nb) köpa liftkort eller båda\nSkirv här: ")
        print("")
        rent_stuff(alternitiv)
    if alternitiv1 == "b":
        return_loan()

if __name__ == "__main__":
    main()

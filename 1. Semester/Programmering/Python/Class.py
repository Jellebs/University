



class profil:   
    __navn: str; 
    __adresse: str; 
    __alder: int; 
    __telefonnummer: int; 
    def __init__(self): 
        self.setup()

    def printAll(self):
        print(f"Navn: {self.__navn}",
            f"\nAdresse: {self.__adresse}",
            f"\nAlder: {self.__alder}",
            f"\nTelefonnummer: {self.__telefonnummer}",
            "\n"
            )
    
        
    def setup(self):
        print("\n\n\n\n\n")
        for i in range(0, 4):
            if i == 0:
                self.__navn = input("Hvad er dit navn: ")
            elif i == 1:
                self.__adresse = input("Hvad er din adresse: ")
            elif i == 2:
                self.__alder = int(input("Hvad er din alder: "))
            elif i == 3:
                self.__telefonnummer = int(input("Hvad er dit telefonnummer: "))
        
person = profil()
person.printAll()

"""
Arbejdsprocess. 
    1. Lav en tamagotchi √
    2. Mulighed for afslut. √
    3. Vis værdier. √
    4. Tidssystem der forringer værdier. √
    5. Funktioner der holder tamagotchien i live. √

    Til tidssystemet har jeg formået at bruge en ekstra tråd, så jeg bruger 2 tråde i det her program.
    Min problemsstilling var, at jeg både vil ønske at kunne interagere med tamagotchien,
    men at jeg også ønskede at kunne køre en timer i baggrunden som opdaterer dens værdier.

    For at ændre tiden det tager for at værdierne ændres, så ændre tickrate værdien. 
    """

import threading
from time import sleep
import os

class Tamagotchi: 
    navn: str = None
    # Værdier der går fra 10 -> 0, ved 0 dør tamagotchien
    humør: int = 10 
    sult: int = 10
    iLive: bool = True
    #livsCyklus: int = 0
    menuMuligheder: str = \
"""Skriv følgende tal for at interagere med tamagotchien
0 - Afslut simulation
1 - Giv fodr
2 - Leg"""

    #Antal sekunder for at værdierne skifter. 
    tickRate = 1

    def __clearTerminal(self): 
        os.system('cls')
        os.system('clear')

    def __init__(self, navn: str): 
        print("Tamagotchien er født!")
        print("Giv den et navn:")
        self.navn = input("")

    def __menu(self): 
        print(self.menuMuligheder)
        
        svar = input()
        muligheder = ['0','1','2']
        while svar not in muligheder: 
            print("Forkert værdi, prøv igen.")
            svar = input()
        if svar == '0' or self.sult == 0 : 
            self.__afslut()
        elif svar == '1': 
            self.__fodr()
        elif svar == '2': 
            self.__leg()

    def __afslut(self): 
        self.iLive = False
        #Afslutter simulationen

    def __fodr(self): 
        #Fodre tamagotchien 
        self.sult += 1
        print("Mums meget bedre, nu er tamagotchien mindre sulten")
        self.__visVærdier()
    
    def __leg(self): 
        #leger med tamagotchien
        self.humør += 1
        print("Juhuuu tamagotchien kom i bedre humør!")
        self.__visVærdier()

    def __vurderVærdi(self, værdi: int, udtrykBedstTilDårligst: list[str]) -> int:
        #vurderer værdier og returnere en score fra 3 til 0
        if værdi == 10: 
            return udtrykBedstTilDårligst[0]
        elif værdi > 6: 
            return udtrykBedstTilDårligst[1]
        elif værdi > 0: 
            return udtrykBedstTilDårligst[2]
        elif værdi == 0: 
            return udtrykBedstTilDårligst[3]

    def __lyt(self, funktion: int) -> str:
        #Lytter til hvordan tamagotchien har sig. 
        # 0 = humør, 1 = sult 
        if funktion == 0:
            return self.__vurderVærdi(self.humør, ["Super godt humør!", "Godt humør", "Dårligt humør", "Deprimeret"])
        elif funktion == 1: 
            return self.__vurderVærdi(self.sult, ["Utrolig mæt", "Mæt", "Sulten", "Død af sult"])        
        else: 
            return "Fejl i lyt"
    
    def __visVærdier(self): 
        #Viser hvordan tamagotchien har det. 
        score: str = f"""
 --------------------------------------
|    Navn:    {self.navn}           
 --------------------------------------
|    Humør:   {self.__lyt(0)}
 --------------------------------------
|    Sult:    {self.__lyt(1)}
 --------------------------------------
"""
        print(score)  
    
    def __sos(self):
        if self.humør == 1: 
            print("Skynd dig at leg med din tamagotchi, den er ved at blive deprimeret")
        if self.sult == 1: 
            print("Skynd dig at fodr din tamagotchi, den er ved at dø!")
        if self.sult == 0: 
            self.iLive = False

    def tid(self):
        def opdater(): 

            sleep(self.tickRate)
            if self.sult != 0: 
                self.__clearTerminal()
                print("\n"*8)
            self.humør -= 1
            self.sult -= 1
            if self.iLive == True: 
                self.__visVærdier()
                if self.sult != 0:
                    print(self.menuMuligheder)
                self.__sos()

        while self.iLive: 
            opdater()

    #def alder():
        #Viser tamagotchiens alder/livscyklus.
    
    def spil(self): 
        #Skal håndtere alle funktioner.    
        tråd1 = threading.Thread(target= self.tid)
        tråd1.start() # Tiden bør køre i baggrunden, menuen skal kunne tilgåes imens. 
        self.__visVærdier()
        while self.iLive:
            self.__menu()
            print("Tamagotchien er i live")
        
        print("Åh nej, tamagotchien døde")

minTamagotchi = Tamagotchi("Kalle") 
minTamagotchi.spil()
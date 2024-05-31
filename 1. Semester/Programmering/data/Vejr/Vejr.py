import os 
import csv
from Data.VejrData import *

#Til Allan:             Fejl og mangler

#Datoerne er forkerte. Datoerne er antaget efter at listen bliver hentet i chronologisk rækkefølge, det gør den ikke. 
#Derfor tror mit program, at der er fejl ved den 7 oktober, som reelt set er den tomme celle fra den 20 oktober.
#Tekst formattet har jeg brugt en del tid på at få til at passe. 
#Det er svært at håndtere kolonner, når hver værdi har forskellige tallængder.

#                       Processen
#Det har været en omvej, at lave klasser før jeg laver listen, har nok været en omvej. 
#Bibliotekter i biblioteker virkede fint, da jeg til sidst skulle lave "Statistik" ud fra classe dataerne. 
#Hvis det bare var for at gøre det hurtigt, så kunne bibliotekter i biblioteker have klaret det hurtigere. 

#Når det så er sagt, så tror jeg, at klasserne også vil kunne have været hurtige,
#hvis jeg ikke skulle have søgt viden indenfor moduler, eller havde stødt på en fejl, som jeg brugte meget tid på. 

#Jeg har lært en del, så er sikker på, at jeg kan klare det hurtigere og bedre næste gang.


#                       Til aflevering. 
#De første 29 -> 62 har med klassehåndtering, som søger i modulet /Data efter timedata og vejrdata
#De sidste 62 - 196 har med skrivning af tekst. 
#Selvom jeg prøvede at implementere funktioner til at hjælpe mig, så var det stadigvæk en masse slavearbejde,
#som krævede meget plads. 

class Vejr: 
    currentDirectory: str = os.getcwd()
    dataDirectory: str = 'Data/vejrdata/'
    folder = os.listdir(currentDirectory+"/"+dataDirectory)
    days: list[VejrData] = [] 
    
    def __init__(self):
        self.main()
    
    def fetchData(self):       
        for i in range(0, len(self.folder)):
            
            vejrData = VejrData(str(i))
            #Opens datafile from a specifik date
            with open(f"{self.dataDirectory}{self.folder[i]}", 'r') as data:      
                try:
                    csvreader = csv.reader(data)
                    datalist = list(csvreader)
                    if len(datalist) < 1: raise Exception("Dokumentet er tomt")
                    x = 0 
                    for row in datalist: 
                        if x == 0: x += 1; continue #For at slippe af med overskrifter.
                        liste = row[0].split(";")
                        time = TimeData(liste)
                        vejrData.addToList(time)
                    self.tilføjTilDage(vejrData)
                except: 
                    print(f"Fejl ved den: {i} Oktober")
                    continue              
    
    def tilføjTilDage(self, vejrData):
        self.days.append(vejrData)


    ## Til at skrive data
    def checkMin(self, nye: float, gamle: float) -> bool:
            if nye < float(gamle): return True
            else: return False

    def checkMax(self, nye: float, gamle: float) -> bool: 
            if nye > float(gamle): return True
            else: return False
            
    def setValue(self,tekst: str, time: TimeData, data):
        match tekst: 
            case "LuftTmp 2m": 
                minDir = data["min"]["tmp2m"]
                maxDir = data["max"]["tmp2m"]
                temperatur = time.luftTmp_2m
                if self.checkMin(temperatur, minDir): data["min"]["tmp2m"] = temperatur
                if self.checkMax(temperatur, maxDir): data["max"]["tmp2m"] = temperatur
                if temperatur < 0.0: data["samlet"]["timerMedFrost"] += 1.0
                data["samlet"]["tmp2m"] += temperatur
                
                
            case "LuftTmp 0m": 
                minDir = data["min"]["tmp0m"]
                maxDir = data["max"]["tmp0m"]
                temperatur = time.luftTmp_0m
                if self.checkMin(temperatur, minDir): data["min"]["tmp0m"] = temperatur 
                if self.checkMax(temperatur, maxDir): data["max"]["tmp0m"] = temperatur
                data["samlet"]["tmp0m"] += temperatur
                
            case "LuftTmp 10cmUnder": 
                minDir = data["min"]["tmp10cmUnder"]
                maxDir = data["max"]["tmp10cmUnder"]
                temperatur = time.luftTmp_0m
                if self.checkMin(temperatur, minDir): data["min"]["tmp10cmUnder"] = temperatur
                if self.checkMax(temperatur, maxDir): data["max"]["tmp10cmUnder"] = temperatur
                data["samlet"]["tmp10cmUnder"] += temperatur
            
            case "Vindhastighed":
                minDir = data["min"]["vindhastighed"]
                maxDir = data["max"]["vindhastighed"]
                vindhastighed = time.vindhastighed_10m
                if self.checkMin(vindhastighed, minDir): data["min"]["vindhastighed"] = vindhastighed
                if self.checkMax(vindhastighed, maxDir): data["max"]["vindhastighed"] = vindhastighed
                data["samlet"]["vindhastighed"] += vindhastighed
            
            case _: 
                print(f"Fejl ved tekst: {tekst}")

                
    def skrivData(self): 
        #Håndter data        
        _ = open("Data redigeret.txt", "w")
        _.write("Data med flere kolonner: Min, max & gennemsnit")
        _.write("\n")
        _.write("|   Dato  |     Temperatur i 2m     |     Temperatur i 0m     | Temperatur 10cm under græsset |Timer med Frost | Timer med nedbør | Samlet nedbør |      Vindhastighed      |")
        _.write("\n")
        _.write("_"*173)
        _.write("\n\n")
        _.close()
        for day in self.days: 
            i = 0
            data = { 
            "samlet": {
                "tmp2m": 0.0,
                "tmp0m": 0.0,
                "tmp10cmUnder": 0.0,
                "vindhastighed": 0.0,
                "timerMedNedbør": 0,
                "nedbør": 0.0, 
                "timerMedFrost": 0
            },
            "min": {
                "tmp2m": 0.0,
                "tmp0m": 0.0,
                "tmp10cmUnder": 0.0, 
                "vindhastighed": 0.0, 
            },
            "max": {
                "tmp2m": 0.0,
                "tmp0m": 0.0,
                "tmp10cmUnder": 0.0, 
                "vindhastighed": 0.0,
            }
        }
            for time in day.timeData():
                if i == 0: i += 1; continue
                self.setValue("LuftTmp 2m", time, data)
                self.setValue("LuftTmp 0m", time, data)
                self.setValue("LuftTmp 10cmUnder", time, data)
                self.setValue("Vindhastighed", time, data)
                if time.nedbør != 0.0: data["samlet"]["timerMedNedbør"] += 1
                data["samlet"]["nedbør"] += time.nedbør
                

            def gennemsnit(værdi: float, antalDage: int)-> float: 
                return float(værdi / antalDage)

            #SkrivData
            
            f = open("Data redigeret.txt", "a")
            f.write("|")
            def skrivVærdi(værdi: float): 
                space: str = ""
                if len(str(værdi)) == 2: space = "    "
                if len(str(værdi)) == 3: space = "   "
                if len(str(værdi)) == 4: space = "  "
                if len(str(værdi)) == 5: space = " "
                f.write(f"{space}{round(værdi, 1)}{space} |")

            if len(str(day.dato())) == 1: f.write(f"    {day.dato()}    |")
            elif len(str(day.dato())) == 2: f.write(f"   {day.dato()}    |")

            skrivVærdi(data["min"]["tmp2m"])
            skrivVærdi(data["max"]["tmp2m"])
            skrivVærdi(gennemsnit(data["samlet"]["tmp2m"], len(self.days)))
            skrivVærdi(data["min"]["tmp0m"])
            skrivVærdi(data["max"]["tmp0m"])
            skrivVærdi(gennemsnit(data["samlet"]["tmp0m"], len(self.days)))
            skrivVærdi(data["min"]["tmp10cmUnder"])
            skrivVærdi(data["max"]["tmp10cmUnder"])
            skrivVærdi(gennemsnit(data["samlet"]["tmp10cmUnder"], len(self.days)))
            skrivVærdi(data["samlet"]["timerMedFrost"])
            skrivVærdi(data["samlet"]["timerMedNedbør"])
            skrivVærdi(data["samlet"]["nedbør"])
            skrivVærdi(data["min"]["vindhastighed"])
            skrivVærdi(data["max"]["vindhastighed"])
            skrivVærdi(gennemsnit(data["samlet"]["vindhastighed"],len(self.days)))    
            f.write("\n\n")
            f.close()
        
    def main(self): 
        self.fetchData()
        self.skrivData()
    
vejr = Vejr()
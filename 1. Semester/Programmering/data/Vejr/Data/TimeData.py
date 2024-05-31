class TimeData: 
    tid: int
    nedbør: float
    luftTmp_2m: float 
    luftTmp_0m: float 
    luftTmp_10cmUnder: float
    vindhastighed_10m: float 

    def __init__(self, liste: list[str]):
        for i in range(0,len(liste)):
            match i: 
                case 0: self.tid = int(liste[0])
                case 1: self.nedbør = float(liste[1])
                case 2: self.luftTmp_2m = float(liste[2])
                case 3: self.luftTmp_0m = float(liste[3])
                case 4: self.luftTmp_10cmUnder = float(liste[4])
                case 5: self.vindhastighed_10m = float(liste[5])
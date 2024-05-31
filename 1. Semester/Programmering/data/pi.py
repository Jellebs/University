with open('pi_million_digits.txt', 'r') as text: 
        data = text.read().rstrip()

class pi: 
    def fødsInPi(self, føds: str): 
        if føds in data: 
            print("Din fødselsdag findes i pi")
        else: 
            print("Din føds er ikke til at finde i pi")
from xmlrpc.client import Boolean


fibListe = [1]
maxTal: int = 1000000
fortsætØnskes: bool = True
print("\n\n")
def fib(x,y):
    if y >= maxTal: 
        return
    fibListe.append(y)   
    fib(y,x+y)

def tjekTal():
    print("\n")
    output = input("Tal:")
    if int(output) in fibListe: 
        print("Tallet er et fibonaccital")
    else: 
        print("Tallet er ikke et fibonaccital")
    
    if output.upper().strip() == "STOP":
        fortsætØnskes = False
        return
    

fib(fibListe[0],1)
def kør(): 
    start = "Indsæt tal til fibonacci tjek. Hvis stop ønskes, skriv \"stop\"" 
    print(start)
    while fortsætØnskes: 
        tjekTal()

kør()

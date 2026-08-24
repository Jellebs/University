
tekst = ["Hej verden", "Har du det godt?"]



# print stile 

def title(tekstsamling):
    print("\n")
    for tekst in tekstsamling:
        print(tekst.title())

def upper(tekstsamling):
    print("\n")
    for tekst in tekstsamling:
        print(tekst.upper())

def lower(tekstsamling):
    print("\n")
    for tekst in tekstsamling:
        print(tekst.lower())

def join(tekstsamling, tab):
    string = ""
    print("\n")
    for tekst in tekstsamling:
        string += tekst
        if tekstsamling[-1] != tekst:
            string += ", "
            if tab == True:
                string += "\t"
    print(string)    

def fjernMellemrum(tekstsamling):
    for tekst in tekstsamling:
        print(tekst.strip())



# print alt
def printout():
#Forkorter tekst til referencen a
    a = tekst
    
    title(a)
    upper(a)
    lower(a)
    join(a, False)
    fjernMellemrum(a)
    join(a, True)
    

# Kør programmet      
printout()




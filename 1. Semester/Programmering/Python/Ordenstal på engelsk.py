
liste = [1+1*i for i in range(100)]
ordensliste = []
print(liste)

for værdi in liste:
    mod = værdi % 10
    string = str(værdi)

    if værdi == 11: 
        string += "th"
    elif værdi == 12: 
        string += "th"
    elif værdi == 13: 
        string += "th"

    elif mod == 3:
        string += "rd"
    elif mod == 2: 
        string += "nd"
    elif mod == 1: 
        string += "st"
    else: 
        string += "th"
    ordensliste.append(string)

print(ordensliste)

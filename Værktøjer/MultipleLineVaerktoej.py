# Bogstaver 

A = ([
    "    ___    ", 
    "   /   \   ",
    "  |     |  ",
    "  /-----\  ",
    " |       | ",
    "_|_     _|_"    
])

B = ([
    " _______   ", 
    "|        \ ",
    "|        / ",
    "|--------  ",
    "|        \ ",
    "|_______ / " 
])
C = ([
    "  ________  ", 
    " /        \ ",
    "|           ",
    "|           ",
    "|           ",
    " \________/ " 
])

D = ([
    " ________  ", 
    "|        \ ",
    "|         |",
    "|         |",
    "|         |",
    "|________/ " 
])
E = ([
    " __________", 
    "|          ",
    "|          ",
    "|------    ",
    "|          ",
    "|__________"   
])

G = ([
    "  _______   ", 
    " /          ",
    "|           ",
    "|      ____ ",
    "|          |",
    " \________/ " 
])
I = ([
    "____________", 
    "      |     ",
    "      |     ",
    "      |     ",
    "      |     ",
    "______|_____"   
])


K = ([
    "_____   ____", 
    "  |    __/  ",
    "  | __/     ",
    "  |/\__     ",
    "  |   \__   ",
    "__|__  __\__"   
])


L = ([
    "___         ", 
    " |          ",
    " |          ",
    " |          ",
    " |       ___",
    "  \_______/ "   
])


M = ([
    " ____    ____ ", 
    "  | \    / |  ",
    "  |  \  /  |  ",
    "  |   \/   |  ",
    "  |        |  ",
    "__|__    __|__"    
])
N = ([
    " _____    _____", 
    "  |  \      |  ",
    "  |   \     |  ",
    "  |    \    |  ",
    "  |     \   |  ",
    "__|__    \__|  "    
])

O = ([
    "  _______  ", 
    " /       \ ",
    "|         |",
    "|         |",
    "|         |",
    " \_______/ " 
])
R = ([
    "   _______     ", 
    "  |        \   ",
    "  |        |   ",
    "  |________/   ",
    "  |        \   ",
    "__|__       \__"   
])
S = ([
    "  __________", 
    " /          ",
    " \          ",
    "  --------  ",
    "          \ ",
    "__________/ "
])

_ = ([
    "            ", 
    "            ", 
    "            ", 
    "            ", 
    "            ", 
    "            ", 
])

def skrivBogstav(bogstav: str, indeks):
    vaerdi = bogstav.upper() 
    match vaerdi:
        case "A": 
            return A[indeks]
        case "B": 
            return B[indeks]
        case "C": 
            return C[indeks]
        case "D": 
            return D[indeks]
        case "E":
            return E[indeks]
        case "G": 
            return G[indeks]
        case "I": 
            return I[indeks]
        case "K": 
            return K[indeks]
        case "L":
            return L[indeks]
        case "M": 
            return M[indeks]
        case "N":
            return N[indeks]
        case "O": 
            return O[indeks]
        case "R": 
            return R[indeks]
        case "S": 
            return S[indeks]
        case " ": 
            return _[indeks]

def printText(text): 
    bogstaver = [*text]
    # """
    rækker = "#"
 
    for i in range(0, len(E)): # Antal rækker
        if i != 0: 
            rækker = "".join([rækker, "\n#"]) # Begynder ny række 
        # rækker = "".join([rækker, skrivBogstav("E", i)]) 
        for bogstav in bogstaver: # Antal bogstavs værdier i rækken.
            rækker = "  ".join([rækker, skrivBogstav(bogstav, indeks=i)])
    if len(rækker)/len(E) > 193: # Teksten fylder for meget til terminalen, jeg laver et tekst dokument til det. 
        fil = open(f"{text}.txt", "x") 
        fil.write(rækker)
    print(len(rækker)/len(E))
    print(rækker)

printText("Diagrammer")
# print("a"*193)
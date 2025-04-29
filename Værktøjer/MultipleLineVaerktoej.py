# Bogstaver 

A = ([
    r"    ___    ", 
    r"   /   \   ",
    r"  |     |  ",
    r"  /-----\  ",
    r" |       | ",
    r"_|_     _|_"    
])

B = ([
    r" _______   ", 
    r"|        \ ",
    r"|        / ",
    r"|--------  ",
    r"|        \ ",
    r"|_______ / " 
])
C = ([
    r"  ________  ", 
    r" /        \ ",
    r"|           ",
    r"|           ",
    r"|           ",
    r" \________/ " 
])

D = ([
    r" ________  ", 
    r"|        \ ",
    r"|         |",
    r"|         |",
    r"|         |",
    r"|________/ " 
])
E = ([
    r" __________", 
    r"|          ",
    r"|          ",
    r"|------    ",
    r"|          ",
    r"|__________"   
])

F = ([
    r" __________", 
    r"|          ",
    r"|          ",
    r"|------    ",
    r"|          ",
    r"|          "   
])

G = ([
    r"  _______   ", 
    r" /          ",
    r"|           ",
    r"|      ____ ",
    r"|          |",
    r" \________/ " 
])
H = ([
    r"_____  _____", 
    r"  |      |  ",
    r"  |      |  ",
    r"  |------|  ",
    r"  |      |  ",
    r"__|__  __|__" 
])
I = ([
    r"____________", 
    r"      |     ",
    r"      |     ",
    r"      |     ",
    r"      |     ",
    r"______|_____"   
])
J = ([
    r"___________ ", 
    r"           |",
    r"           |",
    r"           |",
    r"____       |",
    r"  \_______/ " 
])
K = ([
    r"_____   ____", 
    r"  |    __/  ",
    r"  | __/     ",
    r"  |/\__     ",
    r"  |   \__   ",
    r"__|__  __\__"   
])
L = ([
    r"___         ", 
    r" |          ",
    r" |          ",
    r" |          ",
    r" |       ___",
    r"  \_______/ "   
])


M = ([
    r" ____    ____ ", 
    r"  | \    / |  ",
    r"  |  \  /  |  ",
    r"  |   \/   |  ",
    r"  |        |  ",
    r"__|__    __|__"    
])
N = ([
    r" _____    _____", 
    r"  |  \      |  ",
    r"  |   \     |  ",
    r"  |    \    |  ",
    r"  |     \   |  ",
    r"__|__    \__|  "    
])

O = ([
    r"  _______  ", 
    r" /       \ ",
    r"|         |",
    r"|         |",
    r"|         |",
    r" \_______/ " 
])
P = ([
    r"   _______  ", 
    r"  |       \ ",
    r"  |        |",
    r"  |_______/ ",
    r"  |         ",
    r"__|__       "   
])
R = ([
    r"   _______     ", 
    r"  |        \   ",
    r"  |        |   ",
    r"  |________/   ",
    r"  |        \   ",
    r"__|__       \__"   
])
S = ([
    r"  __________", 
    r" /          ",
    r" \          ",
    r"  --------  ",
    r"          \ ",
    r"__________/ "
])
T = ([
    r"____________", 
    r"      |     ",
    r"      |     ",
    r"      |     ",
    r"      |     ",
    r"     _|_    "   
])
U = ([
    r"___      ___", 
    r" |        |",
    r" |        |",
    r" |        |", 
    r" |        |",
    r"  \______/ "
])
V = ([
    r"__           __", 
    r"  \         /  ",
    r"   \       /   ",
    r"    \     /    ",
    r"     \   /     ",
    r"     _\_/_     "   
])
Æ = ([
    r"____  ______", 
    r" | \ /      ",
    r" |  \       ",
    r" |---\------",
    r" |    \     ",
    r"_|_   _\____"    
])
Ø = ([
    r"  _______/ ", 
    r" /      /\ ",
    r"|     _/  |",
    r"|   _/    |",
    r"|  /      |",
    r" \/______/ " 
])
Å = ([
    r"    ___    ", 
    r"   [___]   ",
    r"    ___    ",
    r"   /   \   ",
    r"  /-----\  ",
    r"_|_     _|_"    
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
        case "F":
            return F[indeks]
        case "G": 
            return G[indeks]
        case "H": 
            return H[indeks]
        case "I": 
            return I[indeks]
        case "J":
            return J[indeks]
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
        case "P": 
            return P[indeks]
        case "R": 
            return R[indeks]
        case "S": 
            return S[indeks]
        case "T": 
            return T[indeks]
        case "U":
            return U[indeks]
        case "V":
            return V[indeks]
        case "Æ":
            return Æ[indeks]
        case "Ø": 
            return Ø[indeks]
        case "Å":
            return Å[indeks]
        case " ": 
            return _[indeks]

def printText(text, linjestarter = "#"): 
    bogstaver = [*text]
    # """
    rækker = linjestarter
 
    for i in range(0, len(E)): # Antal rækker
        if i != 0: 
            rækker = "".join([rækker, "\n" + linjestarter]) # Begynder ny række 
        # rækker = "".join([rækker, skrivBogstav("E", i)]) 
        for bogstav in bogstaver: # Antal bogstavs værdier i rækken.
            # print(skrivBogstav(bogstav, indeks=i))
            rækker = "  ".join([rækker, skrivBogstav(bogstav, indeks=i)])
    if len(rækker)/len(E) > 193: # Teksten fylder for meget til terminalen, jeg laver et tekst dokument til det. 
        fil = open(f"{text}.txt", "x") 
        fil.write(rækker)
    print(len(rækker)/len(E))
    print(rækker)

printText("Hjælpe værktøjer", "#?")

#                           Opgave 5.71 
# Two transistors are needed for an integrated circuit. Of the eight available,
# three have broken insulation layers, two have poor diodes, 
# two have poor diodes, and three are in good condition.
# Two transistors are selected at random.

# a. Find the joint probability distribution of X1 = the number of transistors with broken insulation layers and
#    X2 = the number having poor diodes. 

#    Sandsynligheden for det er  (5 2) / (8 2)  <- (n k)
 
n = 5 # antal mulige
k = 2 # antal successer 

findSandsynlighed <- function(n, k) { 
  sandsynlighed = factorial(n) / (factorial(k)*factorial((n-k)))
  return (sandsynlighed)
}

top = findSandsynlighed(5, 2)
bund = findSandsynlighed(8, 2)

resultat = top/bund
print(resultat)

#    Resultat 
#    2/5 


# Opgave om en sprøjterobot og dens fejl. 

helligdagePrMeterAnden <- 0.8 # Helligdage pr. kvadratmeter 
antalCirkler <- 70 # Forsider på cirklerne
cirkelDiameter <- 1.2 # meter 

# a. Hvor mange fejl må der forventes at være på en cirkel? 
r <- cirkelDiameter / 2 
ArealPrCirkel <- 2 * pi * r**2 # A = 2,26 m^2 

HelligdagePrCirkel <- helligdagePrMeterAnden * ArealPrCirkel # 1,81 Helligdage pr. cirkel




# b. Hvilken sandsynlighedsfordeling vil du bruge til at beskrive antal helligdage på en skive, og hvad er fordelingens middelværdi, varians og standardafvigelse?
# Der er tale om noget per enhed, så her vil det være oplagt at antage at den var poissonfordelt. 

# P(X = x) = (lambda^x)/(x!) * e^(-lambda) 

# Vi kan enten se det som helligdage pr. kvadratmeter, og så finde det totale areal. 
# eller vi kan se på det som helligdage pr. cirkel, og så se på hvor mange cirkler der er. 
# Jeg tror det vil være mest relevant at snakke om pr. cirkel. 

# x = antal cirklers forsider der skal males.

# ===========================================
# Poisonfordelling
Lambda <- HelligdagePrCirkel # ≈1,81 
mu <- Lambda
varians <- Lambda
standardAfvigelse <- sqrt(Lambda)
# ===========================================


# c. Hvad er sandsynligheden for, at ingen af de 70 skiver har helligdage?
# Her passer det jo meget godt, at vi har lambda i cirklernes forside

sandsynlighed <- function(l, x) { # Funktion finder sandsynligheden af fra en poissonfordeling
    # P(X = x), for poissonfordeling
    foersteLed <- l**x
    andetLed <- factorial(x)
    tredjeLed <- exp(-l)
    sandsynlighed <- ((foersteLed / andetLed) * tredjeLed) * 100
    return (sandsynlighed)
}

# pXer0 <- sandsynlighed(Lambda * 70, 0)
pXer0 <- sandsynlighed(Lambda * 70, 0)
# Helligdages gennemsnit for 70 skiver = helligddage pr. skive * 70 = 126,7
# poisson(X = 0) er så udsandsynligt, at vores procenter er i 10^-54



# d. Beregn det forventede antal skiver med henholdsvis 0, 1, 2, 3 og 4 eller flere helligdage.
pXer0 <- sandsynlighed(Lambda, 0)
pXer1 <- sandsynlighed(Lambda, 1)
pXer2 <- sandsynlighed(Lambda, 2)
pXer3 <- sandsynlighed(Lambda, 3)
pXer4EllerFlere <- 100 - (pXer0 + pXer1 + pXer2 + pXer3)
antalMed0 <- (pXer0 / 100) * antalCirkler # Sandsynlighederne er i procent.
antalMed1 <- (pXer1 / 100) * antalCirkler
antalMed2 <- (pXer2 / 100) * antalCirkler
antalMed3 <- (pXer3 / 100) * antalCirkler
antalMed4EllerFlere <- (pXer4EllerFlere / 100) * antalCirkler

O <- matrix(
    c(0, pXer0,           antalMed0, 
      1, pXer1,           antalMed1, 
      2, pXer2,           antalMed2,   # Array med antal observerede
      3, pXer3,           antalMed3,
      4, pXer4EllerFlere, antalMed4EllerFlere),
    nrow = 5,          # Antal rækker
    ncol = 3,          # Antal søjler
    byrow = TRUE      # Data skal læses ind rækkevis (default er søjlevis)
)              
colnames(O) <- c("Antal Helligdage", "Sandsynlighed", "Forventet antal") 

# Mangler stadigvæk nogle dele af opgaven.

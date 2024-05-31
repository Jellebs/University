

# Kapitel 1. Beregn prædiktorer for de studerendes gæt

# Åbn filen med funktionen read.table og skriv resultatet i en matrix D
D = read.table(file.choose(),     # Vælg selv filen i dit filsystem
               header=TRUE,       # Første række er kolonneoverskrifter
               sep=";"            # Værdierne i filen er adskilt af ';'
              )


# Alternativ med direkte sti til fil:
# Set working directory:
# setwd("~/AllanDocs/ECEStat/")
D = read.table("gaet.csv",        # Sti til filen fra working directory
               header=TRUE,       # Første række er kolonneoverskrifter
               sep=";"            # Værdierne i filen er adskilt af ';'
)

x = D$Gaet                        # Vi skal bruge kolonnen med Gæt

middel = mean(x)
varians = var(x)
standafv = sd(x)
minimum = min(x)
maksimum = max(x)
antal = length(x)
medi = median(x)
cv = round(standafv / middel * 100, digits=1)

# NB. Varians med var() giver kun stikprøve-variansen.
# For at få populationsvariansen kan vi gange med (n-1)/n:

popvar = varians*(antal-1)/antal
popstd = sqrt(popvar)
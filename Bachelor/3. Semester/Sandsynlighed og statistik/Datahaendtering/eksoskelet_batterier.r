
## Opgave om batterier til et eksoskelet
## Parallelt boksplot

D = read.table("Kap02/eksoskelet_batterier.csv", header=TRUE, sep=";")

Driftstid = D$Driftstid
Batteritype = D$Batteritype

## a. Middelværdi og standardafvigelse af alle data
y_streg = mean(Driftstid)
std = sd(Driftstid)

## b. Middelværdi og standardafvigelse for hver batteritype
# Data kan opdeles for hver batteritype: 
y_streg_1 = mean(Driftstid[1:5])
# o.s.v.
# Alternativt kan man benytte R-funtionen aggregate: 
y_streg_type = aggregate(x = Driftstid,            # Hvilke data skal der beregnes på?
                         by = list(Batteritype),   # Liste over grupperingen
                         FUN = mean)               # Funktionen, der skal bruges
y_streg_type
# Tilsvarende hvor vi beregner standardafvigelse for hver batteritype: 
std_type = aggregate(x = Driftstid, by = list(Batteritype), FUN = sd)
std_type

## c. Parallelt boksplot
boxplot(Driftstid ~ Batteritype,
        main="Driftstid for tre batterityper",
        xlab="Batteritype",
        ylab="Driftstid (s)"
        )


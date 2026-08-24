D = read.table("exp_hoejde.txt", header = TRUE)
h = D$Hoejde

barplot(h,
        main="Stolpediagram for hoejde i A klassen",
        names.arg = c(1:25), xlab = "Elevnummer",
        ylab = "Hoejde(cm)", ylim = c(0,200), 
        col="#ffe11b")

hist(h,
     main= "Frekvensdiagram for hoejden af elever i A klassen",
     nclass = 4,
     xlab = "Hoejde(cm)",
     ylab = "Antal",
     right = TRUE,     # Til og med eller bare til. TRUE som default.
     col="#2a98ae")   # Frekvensdiagram

stem(h) # Stem and leaf plot

stripchart(h)
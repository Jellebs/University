# setwd("Opgaver/Eksamen/Eksamen 2022/")

sti <- "Data/Data_ECEStat_2022_"
## Opgave 1. 
opg1 <- function() {
    opg1 <- paste(sti, "opg1.csv", sep="")

    ## Data
    d <- read.table(opg1, header = TRUE, sep= ";")
    antalObservationsKategorier <- length(d$Opg1_Observeret_Antal)
    hoejdeFra <- d$Opg1_Hoejde_Fra
    hoejdeTil <- d$Opg1_Hoejde_Til
    observeret <- d$Opg1_Observeret_Antal
    n <- sum(d$Opg1_Observeret_Antal)
    procentDel <- observeret / n * 100

    ## Matrix
    lavMatrix <- function(O, nrow, ncol, colnames) {
        
        O <- matrix(O,
                    nrow = nrow,
                    ncol = ncol,
                    byrow = FALSE)

        colnames(O) <- colnames
        return(O)
    }
    O <- c(hoejdeFra, hoejdeTil, observeret, procentDel, cumsum(procentDel))
    colnames <- c("Hoejde fra", "Hoejde til", "Antal observation", "Procentdel af alle observationer", "Kummuleret procentdel")

    O <- lavMatrix(O, antalObservationsKategorier, 5, colnames = colnames)
    hoejderMidte <- c(0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5)
    hoejdeGennemsnit <- sum((hoejderMidte * observeret)) / n 
}
opg2 <- function() {
    opg2 <- "opg2.csv"
    d <- read.table(paste(sti, opg2, sep=""), header = TRUE, sep=";")
    h <- d$Opg2_Boelgehoejde
    l <- d$Opg2_Boelgelaengde
    e <- d$Opg2_Effekt

    linmod <- lm(e ~ l + h + l:h)
    plotLinReg <- function(x, y, xlab, ylab, titel) {
        par(pty="s") # Gør plottet kvadratisk
        linmod <- lm(y ~ x)
        print(x)
        print(y)
        plot(x, y,
            ratio = 1, 
            type = "p",
            main = titel, 
            xlab = xlab, 
            ylab = ylab, 
            xlim = c(min(x), max(x)), 
            ylim = c(min(y), max(y)), 
            col = "blue")
        
        abline(reg = linmod, col = "red")
    }
    plot(h, e, main = "Effekt af bølgemaskinen", xlab = "Højde", ylab = "Effekt", col = "blue", pch = 16)
    points(l, e, col = "green", pch = 16)

    # e = intercept*slope + l * slope + h * slope + intre

    # abline(linmod, col = "blue")
    # abline(a = -11.344, b = 19.409, col = "red")

    # plotLinReg(l, e, "Bølgelængde", "Effekt", "Effekt af bølgemaskinen")
    # plotLinReg(h, e, "Bølgehøjde", "Effekt", "Effekt af bølgemaskinen")

    d <- data.frame(
        BoelgeHoejde = h[3:9], 
        Effekt = e[3:9]
    )
}

d <- read.table(paste(sti, "opg3.csv", sep=""), header = TRUE, sep=";")
energi <- d$Opg3_Energiproduktion
x <- energi[0:12]
y <- energi[12:24]
boxplot(energi[0:12], energi[12:25])


# Til brug om lidt: 
alpha <- 0.05 
n1 <- length(x)
n2 <- length(y)
df <- n1 + n2 - 2 # observationer minus 2 = Frihedsgrader
s1 <- sd(x)
s2 <- sd(y)
x_mean <- mean(x)
y_mean <- mean(y)

z0 <- (y_mean - x_mean) / (sqrt(s1**2 * 1 / n1 + s2**2 * 1 / n2))
zAlpha <- qnorm(1 - alpha)



t_alphaHalve <- qt(1 - alpha / 2, df) # Den øverste 97,5%
sp <- sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (df)) # Kan ikke huske hvad den står for. 



t0 <- (x_mean - y_mean) / (sp * sqrt(1/n1 + 1/n2))
#setwd("Opgaver/Eksamen/Eksamen 2023")
dataSti <- "Data/Data_ECEStat_2023_"
opg1 <- function() {
    d <- read.table(paste(dataSti, "opg1.csv", sep=""), header = TRUE, sep=";")
    Brembo <- d[1:30, 1:4]
    XBreaking <- d[31:60, 1:4]
    BremboSoft <- Brembo[1:5, 1:4]
    BremboSoft <- rbind(BremboSoft, Brembo[16:20, 1:4])
    BremboMedium <- Brembo[6:10, 1:4]
    BremboMedium <- rbind(BremboMedium, Brembo[21:25, 1:4])
    BremboHard <- Brembo[11:15, 1:4]
    BremboHard <- rbind(BremboHard, Brembo[26:30, 1:4])

    makeArray <- function(startIndeks, liste) {
        type <- liste[startIndeks:(startIndeks + 4), 1:4]
        type <- rbind(type, liste[(startIndeks + 15):(startIndeks + 19), 1:4])
        return(type)
    }
    XBreakingSoft <- makeArray(1, XBreaking)
    XBreakingMedium <- makeArray(6, XBreaking)
    XBreakingHard <- makeArray(11, XBreaking)
    boxplot(BremboHard$Bremseevne, XBreakingHard$Bremseevne, horizontal = TRUE, names = list("Brembo", "X Breaking Systems "))
}

# opg2 <- function() {
mu <- 229
sigma <- 41
sands <- function(nedre, oevre) {
    sands <- pnorm(oevre, mu, sigma) - pnorm(nedre, mu, sigma)
    return(sands)
}
foerste <- pnorm(150, mu, sigma)
anden <- sands(150, 200)
tredje <- sands(200, 250)
fjedre <- sands(250, 300)
femte <- pnorm(300, mu, sigma, lower.tail = FALSE)

d <- read.table(paste(dataSti, "Opg2.csv", sep=""), header=TRUE, sep=";")
TmpInt <- d$Temperaturinterval_tekst

data <- data.frame(
    TemperaturInterval = d$Temperaturinterval_tekst,
    ObserveretAntal = d$ObserveretAntal, 
    PctFraNormalFordeling = c(foerste, anden, tredje, fjedre, femte) 
)
forventet <- function(pct){
    n <- 800
    forventet <- round(n * pct)
    return(forventet)
}
forventetAntal <- 
    c(
        forventet(foerste),
        forventet(anden),
        forventet(tredje),
        forventet(fjedre), 
        forventet(femte)
    )
data$ForventetAntal <- forventetAntal

estimat <- function() {
    n <- 800
    df <- n - 1
    alpha <- 0.05
    chiAlphaHalve <- qchisq(1 - alpha/2, df)
    ChiEnMinusAlphaHalve <- qchisq(alpha/2, n-1)
    KI <- c(df / (chiAlphaHalve**2), df / (ChiEnMinusAlphaHalve**2))
    return(KI)
}
KI <- estimat()

    # Chi^2 test

opg3 <- function() {
    d <- read.table(paste(dataSti, "Opg3.csv", sep = ""), header = TRUE, sep = ";")
    n <- 20
    brembo <- d$Brembo
    brembo_middel <- mean(brembo)
    brembo_sd <- sd(brembo)
    xBS <- d$XBS
    xBS_middel <- mean(xBS)
    xBS_sd <- sd(xBS)
    df <- n - 2 # Frihedsgrader
    alpha <- 0.05
    t_alphaHalve <- qt(1 - alpha / 2, df)

    e_Brembo <- t_alphaHalve * brembo_sd
    e_XBS <- t_alphaHalve * xBS_sd

    kI_Brembo <- c(brembo_middel - e_Brembo, brembo_middel + e_Brembo)
    kI_XBS <- c(xBS_middel - e_XBS, xBS_middel + e_XBS)
    df1 <- n - 1 
    df2 <- df1
    FenMinusAlpha <- qf(1 - alpha / 2, df1, df2)
    Falpha <- qf(alpha / 2, df1, df2)
    F0 <- (xBS_sd**2) / (brembo_sd**2)

    KI <- c(Falpha * F0, FenMinusAlpha * F0)
}


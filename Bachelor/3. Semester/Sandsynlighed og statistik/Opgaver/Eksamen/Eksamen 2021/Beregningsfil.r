# setwd("Opgaver/Eksamen/Eksamen 2021/")
sti <- "Data/Data_ECEStat_2021_"
opg1 <- function() {
    n <- 30
    p <- 0.055 
    p3ellerhoejere <- 1 - dbinom(0, n, p) - dbinom(1, n, p) - dbinom(2, n, p)
    sands <- 1 - pbinom(2, n, p)
}

opg2 <- function() {
    d <- read.table(paste(sti, "opg2.csv", sep = ""), header = TRUE)
    x <- d$Opg2_Tykkelse
    x_middel <- mean(x)
    x_sd <- sd(x)
    n <- 28
    df <- n - 1 
    t_alphaHalve <- function(alpha) { 
        return(qt(1 - alpha / 2, df)) 
    } 
    opgb <- function(alpha) { # KI
        
        E <- t_alphaHalve(alpha) * x_sd
        KI <- c(x_middel - E, x_middel + E)
        return(KI)
    }
    
    opgc <- function(mu) { # t0 
        t0 <- (x_middel - mu)/x_sd
        return(t0)
    }
    opge <- function() { # KI 
        KI <- opgb()
        return(KI)
    } 
    KI <- opgb(0.05) # opgave b
    KI <- opgb(0.01) # opgave e 
    opgf <- function() {
        E <- t_alphaHalve(0.05) * x_sd * sqrt(n) * sqrt(1 + (1 / n)) # estimeringsfejl
        PI <- c(x_middel - E, x_middel + E) # Prædiktionsintervallet
        return(PI)
    }
    PI <- opgf()
    return(PI)
}

d <- read.table(paste(sti, "opg3.csv", sep = ""), sep = ";", header = TRUE) 
A <- d$Opg3_Styrke[1:5]
B <- d$Opg3_Styrke[6:10] 
C <- d$Opg3_Styrke[11:15]
D <- d$Opg3_Styrke[16:20]
data <- data.frame(
    A = A, 
    B = B, 
    C = C, 
    D = D    
)

boxplot(data, main = "Staellegingers styrke", horizontal = TRUE)
test <- data.frame("F0", "A", "B", "C", "D") 
bogstaver <- list("A", "B", "C", "D")
testStoerrelsesTabel <- function() { # F Fordeling
    for (i in 1:4) {
        row <- c(bogstaver[i])
        for (j in 1:4) {
            si <- sd(data[1:5, i])
            sj <- sd(data[1:5, j])
            F0 <- (si**2) / (sj**2)
            row <- c(row, F0)
        }
        test <- rbind(test, row)
    }
}
F_alphaHalve <- qf(0.95, 4, 4)


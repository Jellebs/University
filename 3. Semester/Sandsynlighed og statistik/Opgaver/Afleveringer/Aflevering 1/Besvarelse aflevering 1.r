# Data fra opgaven
# setwd("Afleveringer/Aflevering 1")
print(getwd())
opgave1 <- function() {
    D <- read.table("DataOpg1.csv", header = TRUE) # ./Afleveringer/
    m <- D$solcremeMasse


    # Data behandling
    m_streg <- mean(m)
    m_sd <- sd(m)

    alfa <- 0.05 
    KI <- c(qnorm(alfa / 2, m_streg), qnorm(1 - alfa / 2, m_streg))
    z_alfaHalve <- qnorm(1 - alfa / 2)
    n <- 31 

    KI <- c(qnorm(alfa / 2, m_streg), qnorm(1 - alfa / 2, m_streg))

    print(qnorm(alfa / 2))
}



mu <- 0
sd <- 1
# p1 <- pnorm(-4) + pnorm(4)
p1 <- pnorm(q = -4, mean = 0, sd = 1) + (1 - pnorm(q = 4, mean = 0, sd = 1)) 

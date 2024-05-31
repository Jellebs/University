setwd("../Data")

D = read.table("flymotor.csv", header = TRUE)

tykkelse = D$Tykkelse

quantile(tykkelse)

boxplot(tykkelse,
        main="Boksplot for flymotor godstykkelser",
        horizontal=TRUE,
        xlab="Godstykkelse (in)",
        col="red",
        border="blue"
        )


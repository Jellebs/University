library(png)

plotPNG <- function(filplacering, filnavn) {
    sti = paste(filplacering, filnavn, ".png", sep="")
    billede <- readPNG(sti)
    plot.new()
    rasterImage(billede, 0, 0, 1, 1)
}
#                                   Opgaven om fjedre og deres fjedrekonstanter. 
Fjedrekonstanter <- function() { 
    # Oplysninger fra opgaven
    mu <- 4
    sigma <- 0.1

    # c. P(X > 4.1)
    p_c <- 1 - pnorm(4.1, mu, sigma)

    # d. Interval med 99% af fjedrene 
    x_lav <- qnorm(0.005, mu, sigma)
    x_hoej <- qnorm(1-0.005, mu, sigma) # Alle x op til 99.5% må betyde, at det øverste 0.5% interval må starte her. 

    print(dexp(x <- 6, 4)) # Tæthedsfunktion ud fra lambda. Hvad er sandsynligheden for x 



    # Lav 10 forskellige punkter som er normalfordelte. 
    # Prøv så igen med n <- 1000
    # QQnorm for test om punkter er normalfordelte. 
    n <- 1000 # 10 tilfældige normalfordelte punkter
    middelvaerdi <- 5 
    standardAfvigelse <- 1
    punkter <- rnorm(n, middelvaerdi, standardAfvigelse)
    qqnorm(punkter)

}

#                                   Opgaven om hydralikpumper til eksoskelet.
hydralikpumper <- function() {
    setwd("../Data")
    D <- read.table("eksoskelet_hydralikpumper.csv", header = TRUE)

    x_mean <- mean(D$MaksTrykIBar)
    print(x_mean) # <- 103.125, Får opgaven også.
    # Producenten lover maks pumpetryk på 105. For at være sikre på, at denne antagelse holder, må det være middelværdien.
    mu <- 105
    # For den centrale grænseværdi sætning får vi: x_mean: N(mu, sigma/√n). 
    # Udledes den får vi en normal fordelt funktion fra N(0, 1) som: 

    # Z = (x_mean - mu)/(spredning/(sqrt(n)) )
    standardAfvigelse <- 5.0 
    n <- 8
    Z <- (x_mean - mu)/(spredning/(sqrt(n)))

    # P(X < 4.1) <- pnorm(4.1, mu, sigma)
    # P(X > 4.1) <- 1 - pnorm(4.1, mu, sigma)
    # qnorm <- P(X, x), mu, sigma <-> x. P() invers
    spredning <- standardAfvigelse/sqrt(n)
    sandsynlighed <- pnorm(x_mean, mu, spredning) # X_mean <- Norm(mu, sd/√(n)), so P(X_mean ≤ x_mean) 
    print(sandsynlighed) # <-  14.4%
    # Det samme fik Allan på tavlen.
    # Så 14.4 % af alle pumper har et tryk på 103,125 bar eller mindre. Det lyder ikke usandsynligt

    # Er 8 prøver nok? 
    # Hvis den er nogenlunde normaltfordelt, vil det være tilfældet.
    print(stem(D$MaksTrykIBar)) # Her ses den som normalfordelt.
    punkter <- rnorm(n, mu, spredning)
    qqnorm(punkter) # Normaltfordelt? Så skulle punkterne kunne beskrives med en lige linje. 
    # Hvilket den kan til dels. 
}

#  ___         ________      ____   ________             _________   ________     _______       _______     _______ _____        ____ _____   ___          _____    _________     ________   _______   
# |    \         |   \         /   |                    |           /        \   |       \     |       \   |          |              |       |    \         |      /         \   |          |       \  
# |     \        |    \       /    |                    |          |          |  |        |    |        |  |          |              |       |     \        |     |              |          |        | 
# |      \       |     \     /     |                    |          |          |  |        |    |        |  |          |              |       |      \       |     |              |          |        | 
# |       \      |      \___/      |----                |----      |          |  |_______/     |        |  |----      |              |       |       \      |     |          ___ |----      |_______/  
# |        \     |        |        |                    |          |          |  |        \    |        |  |          |              |       |        \     |     |           |  |          |        \ 
# |         \    |        |        |                    |          |          |  |         \   |        |  |          |              |       |         \    |     |           |  |          |         \ 
#_|_         \___|      __|__      |________          __|__         \________/ __|__        \  |_______/   |________  |________  ____|_____ _|_         \___|      \_________/   |________ _|_        _\_ 

# Sandsynlighed kun med givet middelværdi.
UdslipFraFabrik <- function() {
    #                                   Opgaven om udslip fra en kemisk fabrik. 
    # i denne opgave kender vi ikke både en anslået middelværdi og dens spredning. 
    # Vi får en middelværdi at vide og så må vi estimere spredningen ud fra vores prøver. 

    # Fra fabrikken: 
    mu <- 40 # mg/l

    # Fra stikprøve: 
    x_mean <- 46
    standardAfvigelse <- 9.4 # mg/l
    n <- 20

    # vi kan estimerer en t0, som i stedet for sigma fået af fabrikken er en standardafvigelse fra en stikprøve.
    t0 <- (x_mean-mu)/(standardAfvigelse/sqrt(n))
    # t0 følger en t-fordeling med n - estimater. 
    # Vi har estimeret 1 værdi derfor: 
    t <- n - 1 

    # t-fordelingskommando: 
    sandsynlighed <- (1 - pt(t0, t))*100
    # 1 - P(X) da vi er i den øvre del af fordelingen. 
    print(sandsynlighed) # 0,5% 
    # <-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-
    # 0,5% Er meget usandsynligt at få af en stikprøve, så vi tror ikke på fabrikens påstand. 
    # <-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-

    # For at konkluderer det, må vi også kunne fortælle om fordelingen er nogenlunde normaltfordelt. 
    # Men vi har ikke fået dataene på det, så det kan vi ikke sige mere om. 
}

# Sandsynlighed ud fra spredninger (Chi^2 )

tykkelseAfFolie <- function() {
    #                                   Opgaven om tykkelsen af foliepapir. 
    # Ind i mellem ønsker vi at kunne beskrive sandsynligheden ud fra sigma og standardafvigelserne fra stikprøverne. 
    # Her indfører vi Chi, græsk symbol lignende X 
    # Chi^2 <- ((frihedsgrader)*standardafvigelse^2)/sigma^2
    sigma <- 1.35 # mm pr. folie

    # Der tages jævnligt prøver med 
    n <- 20 # Antal.
    kritiskSpredning <- 1.4 # Her tjekker man maskinen. 
    t <- n - 1 # Frihedsgrader
    Chi0IAnden <- (t*(kritiskSpredning**2))/(sigma**2)
    # print(Chi0IAnden) <- 20.43347
    # t fordlingen med chi laves med 
    sandsynlighed <- (1 - pchisq(Chi0IAnden, t)) * 100 # Sandsynligheden er i den øvre grænse -> 1 - sandsynlighed.
    print(sandsynlighed) # 36.89305% 
    # Med dette kan vi konkluderer at 37% af stikprøverne resulterer i en alarm. 
}

# F fordeling
#                                   Opgave om sammenligning af stikprøver.
stikPrøverFraPopulation <- function() {
    # To stikprøver fra en normalfordelt population tages.
    # Hvad er sandsynligheden for at den første er 3 gange større end den anden?

    # Her kan vi bruge F fordelingen.
    # F <- ((s_1)^2)/(s_2)^2
    # Hvis de er fra samme population og med tilstrækkeligt antal observation regner vi med at
    # F <- 1 

    # Her er F <- 3
    # De har begge hver deres t fordeling. 
    n1 <- 7 
    n2 <- 13 
    # Her har vi en estimeret variabel. 
    t1 <- n1 - 1
    t2 <- n2 - 1
    # Så vi kender F, men vi kender ikke deres spredninger
    # P(F_0 ><- 3), den øvre grænse
    sandsynlighed <- (1 - pf(3, t1, t2)) * 100 # <- 5% 
    print(sandsynlighed) 
}

# Estimering af mu med estimeret standardfejl 
gammelBeton <- function() {
    # Eksempel 7.12 Gammel beton som vejlægning 
    # For beton bruger man parametre til at beskrive hvor elastisk det er. 
    # Måleenheden er hvor meget man skal påvirke materialet med, før at det ikke længere kan komme tilbage til sin oprindelige form. 

    # setwd("./Data")
    # Data givet
    D <- read.table("beton_elasticitet.csv", header = TRUE)
    elasticitet <- D$elasticitetIMPA
    n <- 18
    v <- n - 1 # frihedsgrader

    x_mean <- mean(elasticitet)
    x_standardAfvigelse <- sd(elasticitet)
    x_standardFejl <- x_standardAfvigelse / sqrt(n)
    alpha <- 0.05
    t_alphaHalve <- qt(1 - 0.025, v)
    E <- t_alphaHalve * x_standardFejl # = 9.0
    # Så der kan siges med 1 - alpha = 95% sikkerhed, at estimeringsfejlen højst vil være på 9MPA
}

# Maksimal estimeringsfejl & konfidensinterval 
estimeringsFejl <- function() {
    # En ingeniør vil estimere middelværdien. 
    # Hvad er den maksimale estimeringsfejl med 99% sandsynlighed. 

    # Fra opgaven 
    sigma <- 6.2 
    n <- 150
    alpha <- 1 - 0.99 

    # Z_alpha/2 = z_0.005
    # Så vi kender procentdelen optil punktet, lad os så finde x værdien.
    z_alphaHalve <- qnorm(1 - (alpha / 2))
    x_standardFejl <- sigma / sqrt(n)
    E <- z_alphaHalve * x_standardFejl # = 1.3 
    # Ingeniøren er altså 99% sikker på, at estimeringsfejlen højst vil være på 1.30 

    # Ingeniøren vil med 99% sikkerhed kunne sige, at middelværdien ligger indenfor
    # -E ≤ x_mean ≤ E, så mu = x_mean ± 1.0
    # E skal da højest være 1.0 
    # 1/z_alphaHalve = sigma / sqrt(n)
    # z_alphaHalve = sqrt(n)/sigma
    # z_alphaHalve * sigma = sqrt(n)
    n <- (z_alphaHalve * sigma)**2 # 255.05 
    # Da -E ≤ x_mean ≤ E
    # Må n skulle være større eller lige med vores resultat. n er ikke et heltal, så vi må skulle runde op.
    n <- 256
    x_standardFejl <- sigma / sqrt(n)
    E <- z_alphaHalve * x_standardFejl # = 1.0
}

# Hypotesetest 
hypoteseTest <- function() {
    plotPNG("./Billeder/", "Hypotesetest")

    # En forskergruppe har fundet på et nyt lithiumbatteri til elbiler.
    # De vil gerne påstå, at batteriet kan klare 1600 opladninger. 
    # De tester 36 batterier indtil at de fejler.
    n <- 36

    # Vi opstiller en nul- og alternativhypotese.
    # H0, mu = 1600 nulhypotese 
    # H1, mu > 1600 alternativhypotese

    # type1 fejl: H0 er sand, H0 forkastes. Vi tror at batteriet er langt bedre end det er. Det kunne resulterer i anklager om falske påstande
    # type2 fejl: H1 er sand, H0 accepteres. Vi kan ikke bevise, at batteriet er så godt, som det reelt er, så prisen kan ikke sættes derefter. 

    # alpha = P(H0 forkastes | H0 er sand)
    # vi antager at vi kender standardAfvigelsen som 192

    # For H0
    middelværdiForkastes <- 1660 # x_mean >= 1660
    påståetMiddelværdi <- 1600
    x_standardFejl <- 192 / sqrt(n)


    alpha <- 1 - pnorm(middelværdiForkastes, påståetMiddelværdi, x_standardFejl) 
    # Så der en en 3% chance for, at H0 forkastes i en type 1 fejl. 

    # Hvis alpha sættes som i et konfidensinterval: 
    alpha <- 0.05
    z_alphaHalve <- qnorm(1 - alpha / 2)
    E <- z_alphaHalve * x_standardFejl

    x_oevre <- middelværdiForkastes + E
    x_nedre <- middelværdiForkastes - E
    # Med 95% sikkerhed, kan det med den påståede standard afvigelse siges, at intervallet ligger imellem [1660-62,7; 1660+62,7]

}

toSidetHypoteseTest <- function() {
    # Eksempel side. 249 

    # I en produktion af cementblokke skal blokkene have en termisk konduktivitet på 0.340 
    # Vi vil teste det på 35 blokke, med et 5% significansniveau. 
    # Fra tidligere undersøgelser kendes standardafvigelsen til at være 0.01
    n <- 35
    sigma <- 0.01

    mu <- 0.340 # H0 
    #H1 ≠ 0.340
    alpha <- 0.05
    z_alphaHalve <- qnorm(1 - (alpha / 2))

    # Så hvis z_alphaHalve < z_0 < z_alphaHalve så forkaster vi nul hypotesen. 

    # Fra stikprøven får vi at: 
    x_mean <- 0.343
    z0 <- (x_mean - mu) / (sigma / sqrt(n))

    # -1.96 < z0 = 1.77 < z_alphaHalve = 1.96
    # Derfor kan det med 95% sikkerhed siges, at H0 ikke kan forkastes.
    # n er stor, så den centrale grænseværdisætning burde gælde, og derfor må det være korrekt.
}

# Eksempel 8.7 
# Sammenligning af to stikprøver
# Er det sandsynligt at to stikprøver kommer fra samme population 
stikProeveTest <- function() {
    # Vi antager at forskellen er 0
    delta <- 0 
    n1 <- 6 # Størrelsen af stikprøven.
    n2 <- n1 
    setwd("./Data")
    D <- read.table("C8Ex7.TXT", header=TRUE)
    lokation <- D$location 
    elasticitet <- D$resiliencyMod
    x <- elasticitet[1:6]
    x_streg <- mean(x)
    s1 <- sd(x)
    y <- elasticitet[7:12]
    y_streg <- mean(y)
    s2 <- sd(y)
    df <- n1 + n2 - 2 # t fordeling med to estimater. 
    alfa <- 0.05
    t_alfaHalve <- qt(1 - (alfa / 2), df)
    sp <- sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (df))
    t0 <- (mean(x) - mean(y)) / (sp * sqrt(1 / n1 + 1 / n2))
    # sp = 50,09
    # t0 = 2,65

    # 5. Beslutning
    # Vi forkaster H0, da t0 > t_alfahalve (2.651 > 2.228)
    # Der er forskel på elasticiteten af materialet fra de to 
    # lokaliteter på signifikansniveau 5 %



    qqnorm(x, main='Lokalitet 1')
    # qqline(x)
    qqnorm(y, main='Lokalitet 2')
    # qqline(y)
    # hist(x)
    # hist(y)
    # boxplot(x, y)
    # x og y kommer fra fordelinger, der ligner normalfordelingen. 
    # Samtidig er der ikke stor forskel på s1 og s2, så vi kan gå ud
    # fra, at antagelserne holder



    # p-værdi: 
    p <- 2 * (1 - pt(t0, df)) 
    # p = 0,0243 
    # Hvis H0 var sand, ville vi kun få sådan en i 2.4% af tilfældende, 
    # som er meget usandsynligt. 

    B <- t_alfaHalve * sp * sqrt(1 / n1 + 1 / n2)
    KI <- list(
        x_streg - y_streg - B,
        x_streg - y_streg + B)
    # 95% konfidensinterval = [12.2; 141]
    # 0 er ikke i konfidensintervallet, så vi kan med mere end 95% sandsynlighed sige
    # at 0 ikke er i intervallet.

    res <- t.test(x, y,                 # data; de to stikprøver
        alternative = "two.sided",    # Vi har <> i H1 (dflt)
        mu = 0,                       # Værdien af delta0
        conf.level = 0.95,          # 1 - alfa
        var.equal = TRUE,             # sørger for at sp bruges
        )
    print(res)
}

# Eksempel 8.12 
tabteArbejdstimer <- function() {
    #Indlæser data:
    setwd("./Data")
    M = read.delim("C8Ex12.TXT", header=TRUE)
    x = M$Before   
    y = M$After

    delta0 = 0
    n = 10
    alfa = 0.05

    #########################################
    # PARRET T-TEST

    d = x-y
    d_streg = mean(d)
    s_d = sd(d)

    # 1. Hypoteser
    # H0: delta = delta0 = 0
    # H1: delta > 0 (<> betyder her 'forskellig fra')

    # 2. Signifikansniveau
    # Alfa er 0.05

    # 3. Kriterier
    # Teststørrelsen 
    # t0 = (d_streg - delta0)/(s_d/sqrt(n))
    # t0 er t-fordelt med n-1 frihedsgrader

    # Vi forkaster H0, hvis t0 > t_alfa, 
    # hvor 
    t_alfa = qt(1-alfa, n-1)
    # t_alfa = 1.833

    # 4. Beregn teststørrelsen
    t0 = (d_streg - delta0)/(s_d/sqrt(n))
    # t0 = 4.033

    # 5. Beslutning
    # Vi forkaster H0, da t0 > t_alfa (4.033 > 1.833)
    # Der er forskel på sikkerheden før og efter indførelsen af 
    # sikkerhedspakken på signifikansniveau 5 %
    p_vaerdi = 1 - pt(t0, n-1)
    # p_vaerdi = 0.00148


    #########################################
    # To uafhængige stikprøver

    # Oplysninger fra opgaven:
    n1 = n
    n2 = n

    # Beregninger af data:
    x_streg = mean(x)
    s1 = sd(x)
    y_streg = mean(y)
    s2 = sd(y)

    # 1. Hypoteser
    # H0: mu1 - mu2 = delta0 = 0
    # H1: mu1 - mu2 > 0 (flere mistede timer før)

    # 2. Signifikansniveau
    # Alfa er 0.05

    # 3. Kriterier
    # Teststørrelsen 
    # t0 = (x_streg - y_streg - delta0)/(sp*sqrt(1/n1 + 1/n2))
    # hvor sp er den puljede standardafvigelse:
    # sp = ((n1-1)*s1^2 + (n2-1)*s2^2)/(n1+n2-2)
    # t0 er t-fordelt med n1+n2-2 frihedsgrader
    df = n1+n2-2

    # Vi forkaster H0, hvis t0 > t_alfa, hvor 
    t_alfa = qt(1-alfa, df)
    # t_alfa = 1.734

    # 4. Beregn teststørrelsen
    sp = sqrt(((n1-1)*s1^2 + (n2-1)*s2^2)/(n1+n2-2))
    t0 = (x_streg - y_streg - delta0)/(sp*sqrt(1/n1 + 1/n2))
    # sp = 31.55
    # t0 = 0.369

    # 5. Beslutning
    # Vi kan ikke forkaste H0, da t0 < t_alfa (0.369 < 1.734)
    # Der er er ikke signifikant forskel på antal mistede arbejdstimer 
    # som følge af ulykker før og efter sikkerhedspakken på signifikans-
    # niveau 5 %
    #
    p_vaerdi = qt(1-t0, df)
    # p_vaerdi = 0.34

    # p-værdi
    boxplot(x, y,
            horizontal=TRUE,
            names= c("Før","Efter"), 
            main="Tabte arbejdstimer pr. uge pga. ulykker"
    )
}

# Eksempel 9.2. s292

# I en osteproduktion tages en stikprøve med vægten 
osteproduktion <- function() {
    n <- 80 
    # Man ønsker x_streg = 68,45 og s = 9,583 til at lave et konfidensinterval
    # Der antages at vægten af ostene er normalfordelt
    df <- n - 1 # Frihedsgrader
    alfa <- 0.05
    chiIAnden_alfaHalve <- qhisq(1 - (alfa / 2), df)
    chiIAnden_EnMinusAlfaHalve <- qhicsq(alfa / 2, df)

}


# Chi^2 hypotesetest
# Eksempel 10.13 og 10.14. Kontingenstabel. 
# Sammenhængen mellem styrketræning og at klare sig godt på arbejdet.

chiIAnden_HypoteseTest <- function() {
    r <- 3            # Antal rækker
    c <- 3            # Antal søjler
    # Jeg bruger matrix() til at indlæse data, så jeg lettere kan 
    # beregne forventet antal 
    O <- matrix(
        c(23, 60, 29, 
          28, 79, 60, 
          9, 49, 63),   # Array med antal observerede
        nrow = r,          # Antal rækker
        ncol = c,          # Antal søjler
        byrow = TRUE       # Data skal læses ind rækkevis (default
    )                # er søjlevis)
    print(O)
    n <- sum(O)                  # Tjekker, at n <- 400

    ## 1. Hypoteser
    # H0: Performance i job og træningsprogram er uafhængige
    # H1: Der er ikke uafhængige

    ## 2. Signifikansniveau
    alfa <- 0.01 # 99% sikkerhed

    ## 3. Kriterier
    # chi2_0 <- sum((E-O)^2/E) er chi-i-anden fordelt med (r-1)*(c-1) 
    # frihedsgrader.
    # Vi forkaster nulhypotesen hvis chi2_0 > chi2_alfa
    df <- (r - 1) * (c - 1)
    chi2_alfa <- qchisq(1 - alfa, df)
    # chi2_alfa <- 13.277

    egenTest <- function(O, chiAlfa) {
        

        ## 4. Beregninger
        # Vi har brug for at beregne forventet antal, E.
        # Da data er repræsenteret i en matrix kan jeg beregne 
        # rækkesummer og søjlesummer som hhv 2x1 og 1x2 matricer
        rsum <- matrix(rowSums(O), nrow = r)  # Sum af elementer i hver række af O
        ssum <- matrix(colSums(O), ncol = c)  # Sum af elementer i hver søjle af O
        print(rsum)
        print(ssum)

        # Beregning af forventet antal i matricen E
        # E_ij <- rsum_i*ssum_j/n
        # matrix-multiplikation i R sker med operatoren %*%
        E <- rsum %*% ssum / n    
        print(E)

        # Nu er vi klar til at beregne teststørrelsen chi2_0:
        chi2_0 <- sum((E-O)^2/E)
        # chi2_0 <- 20.1789
        afhængighed <- chi2_0 <= chiAlfa # ? 

    }
    rHypoteseTest <- function(O, chiAlfa) {
        ## Alternativ løsning med R funktionen chisq.test()
        res <- chisq.test(
            O,
            correct = FALSE  # Vi skal undgå, at R laver en korrektion
        )
        print(res)
        E <- res$expected

        print(E)
        print(O)
        chi2_0 <- sum((E - O)^2 / E)
        
        afhængighed <- chi2_0 <= chiAlfa # ? 
    }
    
    ## 5. Konklusion
    # Da teststørrelsen chi2_0 <- 20.1789 er større end den kritiske 
    # grænse chi2_alfa <- 13.27, må vi forkaste nulhypotesen. Dermed er 
    # der afhængighed mellem hvordan man klarer sig i træningsprogrammet
    # og i jobbet.
}






#     _______        __________    _______        _______        __________    __________    __________  ____________    ___________       ___      _____
#    |        \     |             /              |        \     |             /             /                  |        /           \     |    \      |  
#    |        |     |            |               |        |     |             \             \                  |       |             |    |     \     |  
#    |________/     |------      |      ____     |________/     |------        --------      --------          |       |             |    |      \    |  
#    |        \     |            |          |    |        \     |                      \             \         |       |             |    |       \   |  
#  __|__       \__  |__________   \________/   __|__       \__  |__________  __________/   __________/   ______|_____   \___________/   __|__      \__|  


# Lineært regression

# Nedkøling af legering
# Eks 11. 1, s.331
# Mindste kvadratters metode

nedKoelingAfLegering <- function() {
    setwd("./Data")
    D <- read.delim("C11coolingr.TXT", header = TRUE)
    x <- D$x
    y <- D$y
    n <- 8 
    # Standard fejl 
    Sxy <- sum(x * y) - 1 / n * sum(x) * sum(y)
    Sxx <- sum(x**2) - 1 / n * sum(x)**2

    # Så kan man da få hældningen som Sxy / Sxx
    b1 <- Sxy / Sxx

    # Skæring med y aksen = x_mean
    x_mean <- 1 / n * sum(x)
    y_mean <- 1 / n * sum(y)
    b0 <- y_mean - b1 * x_mean

    # ============================
    # y_hat <- b0 + b1x <- 22 + 6x
    # ============================

    # Eller kan løses ved ligningssystemet
    #      b0x      b1x         =    y 
    #A <- Matrix(
    #       c(     n * b0,    b1 * sum(x), sum(y)),
    #       c(b0 * sum(x), b1 * sum(x**2), sum(x*y))
    #     )



    # En anden måde at finde den lineære regression på. 
    linmod <- lm(y ~ x)
    summary(linmod)

    # Scatter plot med regression
    plot(x, y, type = "p",
        main = "Nedkølingsratens afhængighed af tilsat komponent", 
        xlab = "Tilsat komponent (%)", 
        ylab = "Nedkølingshastighed (F/time)", 
        ylim = c(0, 70), 
        col = "blue")
    abline(reg = linmod, col = "red")
}

# Nanosøjler af silicone
# Eks. 11.3, s.333
# I nanoteknologi bruges nanosøjler af silicone. 
# Man har målt bredde (x) og højde (y) af 50 nanosøjler.
nanosoejlerAfSc <- function() {
    n <- 50 
    x_mean <- 88.34
    y_mean <- 305.58

    Sxx <- 7239
    Sxy <- 17840 
    Syy <- 66976

    # a. Lav en lineær regression, der forudsiger højde fra bredde 
    b1y <- Sxy / Sxx # Hældning a = y/x 

    b0y <- y_mean - b1 * x_mean

    # =================================
    # y_hat <- b0 + b1x <- 87,9 + 2,46x 
    # ================================= 



    # b. Lav en lineær regression, der forudsiger bredde fra højde
    # Så må det vel være modsat, så vi ønsker at finde x_hat

    b1x <- Sxy / Syy # a = x/y 
    b0x <- x_mean - b1 * y_mean 

    # =================================
    # x_hat <- b0 + b1y <- -35,7 + 0,406y 
    # ================================= 


    # c. Hvis begge regressionslinjer på et scatter plot.
    # splot()
    # abline(coef = c(b0x, b1x))
    # abline(coef = c(b0y, b1y))

    # Jeg slutter på side 40 på slidsne til kapitel 11.
}







####            Multipel lineær regression  ( ANOVA )            ####


# Regression i forhold til 2 variabler
# Eksempel 13.1 s. 428 ( vejbelægning )
vejbelægning <- function() {
    # Genbrug af byggematerialer og der ønskes at vides med en signifikansniveau på 1%, hvor elastisk materialet stadigvæk er. 

    # Faktor A, Lokalitet 
    # Faktor B, type af materiale
    # Resultat, elasticitet
    # setwd("././Data")

    d <- read.table("C13Ex1.TXT", header = TRUE)
    res <- d$resilmod
    lok <- d$A
    mat <- d$B

    alpha <- 0.01
    fm1 <- aov(res ~ lok + mat + lok:mat)
    # Skriv summary(fm1) i interactive terminal
    TukeyHSD(fm1, conf.level = 0.99)
}




# Eksempel fra video, karakterer af elever: 
# https://www.youtube.com/watch?v=1iRC_MbzOGQ
# setwd("././Data")
d <- read.table("Ch18_GGPA_1.txt", header = TRUE)



import pandas as pd


df = pd.DataFrame()
# df = pd.read_excel(fil, engine = "openpyxl")

df["Måned(er)"] = [1]

måneder = 24

månedligAfbetaling = 7000
rente = 0.04

beløbOmMåneden = [1000, 1500, 2000, 2500, 3000]

def opsætKolonne(df, alleBeløb):
    i = 1 
    for beløb in alleBeløb: 
        df[f"Lånt ({beløb})"] = [beløb]
        df[f"Skylder ({beløb})"] = [beløb]
        df[f"Afbetalt ({beløb})"] = [0]
        df[i*" "] = "" # Tom kolonne.
        i+=1 

def opdaterRækker(df, alleBeløb): 
    for i in range(1, måneder): 
        df.loc[i, "Måned(er)"] = i+1
        for beløb in alleBeløb: 
            df.loc[i, f"Afbetalt ({beløb})"] = 0
            df[f"Lånt ({beløb})"] = df.loc[i - 1, f"Lånt ({beløb})"] + beløb
            nyværdi = (df.loc[i-1, f"Skylder ({beløb})"] + beløb) * (1 + rente)
            df.loc[i, f"Skylder ({beløb})"] = nyværdi 

def afbetaling(df, alleBeløb):
    for i in range(måneder, 48): 
        måned = i - måneder + 1
        df.loc[i, "Måned(er)"] = i
        
        for beløb in alleBeløb: 
            if df.loc[i - 1, f"Skylder ({beløb})"] <= 0: 
                df.loc[i, f"Skylder ({beløb})"] = 0
                continue
            elif df.loc[i - 1, f"Skylder ({beløb})"] <= månedligAfbetaling: 
                df.loc[i, f"Afbetalt ({beløb})"] = df.loc[i - 1, f"Afbetalt ({beløb})"] + df.loc[i - 1, f"Skylder ({beløb})"]
                df.loc[i, f"Skylder ({beløb})"] = 0
                continue
            
            df.loc[i, f"Afbetalt ({beløb})"] = måned * månedligAfbetaling
            nyværdi = (df.loc[i-1, f"Skylder ({beløb})"] - månedligAfbetaling) * (1 + rente)
            df.loc[i, f"Skylder ({beløb})"] = nyværdi 
 
    
opsætKolonne(df, beløbOmMåneden)
opdaterRækker(df, beløbOmMåneden)
afbetaling(df, beløbOmMåneden)

fil = "SULån.xlsx"
df.to_excel(fil, index=False)
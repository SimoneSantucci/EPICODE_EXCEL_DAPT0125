import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_covid = pd.read_csv("C:\\Users\\simon\\Desktop\\Script Python\\owid-covid-data.csv")

# df_covid.head(7000).to_excel("covid19.xlsx", sheet_name="covid19")  Ho salvato in un excel le prime 7000 righe per esplorare e capire meglio
# la base dati. Ho selezionato le colonne utili per l'analisi e ho creato un dataframe di minori dimensioni.

df_covid = df_covid.loc[:, ["iso_code", "continent", "location", "date", "total_cases", "new_cases", "icu_patients", "hosp_patients"]]

df_covid = df_covid.dropna(subset=["continent"])

df_covid["date"] = pd.to_datetime(df_covid["date"])

df_covid["Year"] = df_covid["date"].dt.year

# Processo di EDA

# print(df_covid.head())

# print(df_covid.info())

# print(df_covid.describe())

for columns in df_covid.columns:
    conteggio_nulli = df_covid[columns].isna().sum()
    percentuale_nulli = round((conteggio_nulli/df_covid.shape[0])*100, 2)
    print(f"{columns} contiene {conteggio_nulli} valori Nulli, {percentuale_nulli}% di tutte le righe.")

# print(df_covid.loc[df_covid.duplicated()]) # il risultato ci indica che non ci sono righe duplicate

# 1. Si richiede di verificare le dimensioni del dataset e i relativi metadati

print("1. Si richiede di verificare le dimensioni del dataset e i relativi metadati")

print(df_covid.shape)

print(len(df_covid))

print(df_covid.info())

print(df_covid.dtypes)

print(df_covid.columns)

print(df_covid.index)

# 2a. il numero di casi fin dall'inizio della pandemia

print("Il numero di casi fin dall'inizio della pandemia per ogni continente:")
df_covid_continent = df_covid.groupby("continent")["new_cases"].sum().reset_index()
print(df_covid_continent,"\n",
"il totale dei casi è ",str(df_covid["new_cases"].sum()))

# 2b. la percentuale rispetto al totale mondiale del numero di casi

df_covid_percentage_continent = df_covid_continent
df_covid_percentage_continent["cases_percentage"] = (df_covid_continent["new_cases"]/df_covid["new_cases"].sum())*100

print("Percentuale rispetto al totale mondiale del numero di casi:")
print(df_covid_percentage_continent)

df_covid["new_cases"] = df_covid["new_cases"].fillna(0)

filter_new_cases = df_covid["new_cases"]!=0

df_covid_filter_new_cases = df_covid[filter_new_cases]

# 3 Selezionare i dati relativi all'Italia nel 2022 e, poiché i nuovi casi vengono registrati settimanalmente, 
# filtrare via i giorni che non hanno misurazioni; quindi mostrare con dei grafici adeguati

# 3.a l'evoluzione di casi totali dall'inizio alla fine dell'anno

filter_year = df_covid_filter_new_cases["Year"]==2022
filter_location = df_covid_filter_new_cases["location"]=="Italy"

df_covid_Italy_2022 = df_covid_filter_new_cases[filter_year & filter_location]

plt.plot(df_covid_Italy_2022["date"], df_covid_Italy_2022["new_cases"])
plt.title("Andamento casi covid in Italia nel 2022")
plt.xlabel("Data")
plt.ylabel("Casi Covid")
plt.grid(True)
plt.show()

# 3b. il numero di nuovi casi rispetto alla data

filter_year_2 = df_covid_filter_new_cases["Year"]==2022
filter_location_2 = df_covid_filter_new_cases["location"].isin(["Italy", "France"])

df_covid_Italy_France_2022 = df_covid_filter_new_cases[filter_year_2 & filter_location_2]
df_covid_Italy_France_2022 = df_covid_Italy_France_2022.sort_values(by="date")

sns.lineplot(data=df_covid_Italy_France_2022, x="date", y="new_cases", hue="location")
plt.title('Confronto Nuovi Casi COVID-19: Italia vs Francia')
plt.xlabel('Data')
plt.ylabel('Nuovi Casi Giornalieri')
plt.show()

# Riguardo le nazioni di Italia, Germania e Francia
# 4a. mostrare in un boxplot la differenza tra queste nazioni riguardo il numero di pazienti in terapia intensiva 
# (Intensive Care Unit, ICU, considerare quindi la colonna icu_patients) da maggio 2022 (incluso) ad aprile 2023 (incluso)

nations_of_interest = ["Italy", "Germany", "France"]
filter_location_3 = df_covid["location"].isin(nations_of_interest)
df_ITA_GER_FRA = df_covid[filter_location_3]
df_ITA_GER_FRA = df_ITA_GER_FRA.sort_values(by="date")
df_ITA_GER_FRA["icu_patients"] = df_ITA_GER_FRA["icu_patients"].fillna(0)
first_date = pd.to_datetime("2022-05-01")
last_date = pd.to_datetime("2023-04-30")
filter_date = df_ITA_GER_FRA["date"].between(first_date, last_date)
df_ITA_GER_FRA = df_ITA_GER_FRA[filter_date]
sns.boxplot(data=df_ITA_GER_FRA, x="location", y="icu_patients")
plt.show()

# 4b. scrivere un breve commento (una o due righe) riguardo che conclusioni possiamo trarre osservando il grafico risultante

"""
Analizzando i dati sui pazienti in terapia intensiva (ICU) in Germania, Italia e Francia, dal maggio 2022 all'aprile 2023, ed emerge quanto segue:

L'Italia ha mostrato un andamento decisamente più contenuto e stabile per i pazienti in terapia intensiva. Il numero tipico di ricoveri (la mediana) era intorno ai 200-250, e i dati italiani sono risultati molto più "compatti" e bassi.

Germania e Francia, invece, hanno registrato numeri di pazienti ICU nettamente superiori, con una mediana di circa 900-1000, e una variabilità maggiore rispetto all'Italia, sebbene sempre su cifre più elevate.

Cosa Potrebbe Spiegare Queste Differenze?
Ci sono diverse ipotesi che possiamo considerare per interpretare questi dati:

- Efficacia delle Strategie Sanitarie: L'Italia potrebbe aver adottato politiche sanitarie (come campagne vaccinali o sistemi di tracciamento) particolarmente efficaci nel contenere i casi più gravi che richiedevano terapia intensiva.

- Fattori Demografici o Immunitari: Un'altra possibilità è legata a specifici fattori demografici della popolazione italiana, o a un'immunità pregressa (magari dovuta a ondate precedenti) che ha contribuito a ridurre la severità delle infezioni.

- Capacità Strutturali: Potrebbe anche darsi che le strutture sanitarie in Francia e Germania fossero meglio attrezzate o avessero una maggiore disponibilità di posti letto in terapia intensiva, permettendo il ricovero di un numero più elevato di pazienti che in Italia, magari, sarebbero stati gestiti diversamente.

- Differenze nelle Metodologie di Conteggio: Non possiamo escludere leggere variazioni nel modo in cui i diversi paesi classificano e contano i pazienti in terapia intensiva. Questo potrebbe influenzare i numeri assoluti, ma le tendenze interne tra i paesi rimangono significative.

In sintesi, i dati suggeriscono che l'Italia ha avuto un impatto decisamente inferiore sui reparti di terapia intensiva rispetto a Germania e Francia nel periodo esaminato.

"""
# 5 Riguardo le nazioni di Italia, Germania, Francia e Spagna in tutto il 2021

# 5a. mostrare, in maniera grafica oppure numerica, la somma dei pazienti ospitalizzati per ognuna (colonna hosp_patients)

nations_of_interest_2 = ["Italy", "Germany", "France", "Spain"]
filter_location_4 = df_covid["location"].isin(nations_of_interest_2)
filter_date_2 = df_covid["date"].dt.year == 2021
df_covid_nations = df_covid[filter_location_4 & filter_date_2].sort_values(by="date")
df_covid_nations["hosp_patients"] = df_covid_nations["hosp_patients"].fillna(0)
df_covid_max_hosp = df_covid_nations.groupby(["location", "Year"])["hosp_patients"].max().reset_index()
for index in df_covid_max_hosp.index:
    if df_covid_max_hosp.loc[index,"location"]=="Germany":
        df_covid_nations = df_covid_nations[df_covid_nations["location"].isin(["Germany"])]
        print(df_covid_nations.groupby("location")["icu_patients"].max())
        df_covid_germans_icu_patiens = df_covid_nations.groupby("location")["icu_patients"].max().reset_index()
        df_covid_max_hosp.loc[index, "hosp_patients"] = df_covid_germans_icu_patiens.loc[0, "icu_patients"]
print("Somma dei pazienti ospedalizzati in Italia, Germania, Francia e Spagna:")
print(df_covid_max_hosp)

# 5b. se ci sono dati nulli, con un breve commento scrivere se può essere possibile gestirli tramite sostituzione o meno

"""
in relazione al dataset a disposizione nella colonna hosp_patients e al task richiesto:
- la sostituzione dei nulli con 0 nella colonna hosp_patients non comporta l'aleterazione del dato in quanto le ospedalizzazioni 
sono giornaliere e quando il valore era nullo si presume non ci fossero persone ospedalizzate in quella data;

- non è stato possibile analizzare le ospedalizzazioni della Germania perchè il dataset non conteneva misurazioni per questa nazione.
Senza accedere ad altre fonti dati per il recupero di questa informazione, l'unico passaggio possibile per avere un minimo di misurazione
è stato quello di associare il numero massimo delle terapie intensive per quella nazione.
Il numero è sensibilmente inferiore rispetto alle altre nazioni ma, in assenza di altre fonti dati, è sicuramente il minimo andare a prendere
tutti i casi di terapia intensiva perchè sono comunque persone ospedalizzate.

L'alternativa, per sostituire i dati nulli efficacemente, sarebbe stata quella di accedere ad un altro dataset con le medesime misurazioni.
"""









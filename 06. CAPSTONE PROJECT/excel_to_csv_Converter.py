import pandas as pd
import os

# Chiede all'utente il percorso del file Excel
excel_file = input("Inserisci il percorso completo del file Excel: ")

# Chiede all'utente la cartella di output per i CSV
output_folder = input("Inserisci il percorso della cartella dove salvare i CSV: ")
os.makedirs(output_folder, exist_ok=True)

# Legge tutti i fogli in un dizionario
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Ciclo su ogni foglio
for sheet_name, df in all_sheets.items():
    # Crea un nome di file CSV sicuro
    csv_file_name = f"{sheet_name}.csv".replace(" ", "_")
    csv_path = os.path.join(output_folder, csv_file_name)
    
    # Salva in CSV, separatore virgola, codifica UTF-8
    df.to_csv(csv_path, index=False, sep=",", encoding="utf-8")
    
    print(f"Salvato: {csv_path}")
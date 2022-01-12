# Predavanje 3 — CSV Fajlovi i os.path

## 3.1 CSV modul

```python
import csv

# Pisanje
with open("podaci.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Ime", "Godine", "Grad"])
    writer.writerow(["Vahid", 34, "Novi Pazar"])

# Čitanje
with open("podaci.csv", "r") as f:
    reader = csv.reader(f)
    for red in reader:
        print(red)
```

## 3.2 os.path za rad sa putanjama

| Funkcija | Opis |
|---|---|
| `os.path.exists(p)` | Da li putanja postoji? |
| `os.path.isfile(p)` | Da li je fajl? |
| `os.path.isdir(p)` | Da li je direktorijum? |
| `os.path.join(a, b)` | Spaja delove putanje |
| `os.listdir(p)` | Lista fajlova u direktorijumu |

## Rezime
- `csv.writer/reader` za tabelarne podatke
- `os.path` za bezbedno upravljanje putanjama
- `os.makedirs(path, exist_ok=True)` za kreiranje direktorijuma

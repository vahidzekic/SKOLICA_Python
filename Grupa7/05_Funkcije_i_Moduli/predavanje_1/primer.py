#!/usr/bin/env python3
# Grupa7 / 05 / P1 â Funkcije

def km_to_mi(km):
    return round(km * 0.621371, 2)

def vreme_putovanja(km, brzina=100):
    sati = km / brzina
    h = int(sati)
    m = int((sati - h) * 60)
    return f"{h}h {m}min"

def trip_stats(*udaljenosti):
    if not udaljenosti: return {}
    return {"ukupno": sum(udaljenosti), "prosek": round(sum(udaljenosti)/len(udaljenosti)), "etapa": len(udaljenosti)}

def trip_card(**kw):
    for k, v in kw.items():
        print(f"  {k}: {v}")

print(f"594km = {km_to_mi(594)}mi")
print(f"Vreme: {vreme_putovanja(594, 120)}")
print(f"Stats: {trip_stats(594, 1060, 1700)}")
print("\nTrip:")
trip_card(destinacija="Istanbul", transport="Avion", cena="200 EUR")
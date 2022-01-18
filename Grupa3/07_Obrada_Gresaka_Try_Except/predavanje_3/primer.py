#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 07_Obrada_Gresaka_Try_Except / Predavanje 3
# Tema: Logging, debugging obrasci, robust kod
# =============================================================================
import logging
import os

# --- Konfiguracija loggera ---
os.makedirs("data", exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("data/app.log", encoding="utf-8")
    ]
)
logger = logging.getLogger("SKOLICA")

# --- 1. NIVOI LOGOVANJA ---
print("=== Nivoi logovanja ===")
logger.debug("Ovo je DEBUG poruka")
logger.info("Aplikacija pokrenuta")
logger.warning("Disk je 80% popunjen")
logger.error("Konekcija sa bazom neuspešna")
print("")

# --- 2. ROBUST FUNKCIJA SA LOGOVANJEM ---
def bezbedan_unos(prompt, tip=int, ponude=3):
    for pokusaj in range(1, ponude + 1):
        try:
            vrednost = tip(input(prompt))
            logger.info(f"Uspešan unos: {vrednost}")
            return vrednost
        except ValueError:
            logger.warning(f"Neispravan unos (pokušaj {pokusaj}/{ponude})")
    logger.error("Prekoračen broj pokušaja")
    return None

print("=== Robust unos ===")
broj = bezbedan_unos("Unesite ceo broj: ", int, ponude=3)
if broj is not None:
    print(f"Uneli ste: {broj}")
else:
    print("Niste uneli validan broj.")

print("\n✅ Log zapisan u data/app.log")

#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 10_Regularni_Izrazi_RegEx / Predavanje 3
# Tema: Praktična primena — parsiranje, čišćenje, ekstrakcija
# =============================================================================
import re

# --- 1. ČIŠĆENJE TEKSTA ---
print("=== Čišćenje teksta ===")
neuredjen = "  Ovo   je    neuredan   tekst  sa    razmacima.  "
ociscen = re.sub(r"\s+", " ", neuredjen).strip()
print(f"  Pre: '{neuredjen}'")
print(f"  Posle: '{ociscen}'")
print("")

# --- 2. PARSIRANJE LOG FAJLA ---
print("=== Parsiranje loga ===")
log_linije = [
    "2024-01-15 08:30:00 [INFO] Server pokrenut",
    "2024-01-15 08:31:15 [ERROR] Baza nedostupna",
    "2024-01-15 08:32:00 [INFO] Ponovna konekcija",
    "2024-01-15 08:33:45 [WARNING] Visoka upotreba memorije",
]

obrazac = r"(?P<datum>[\d-]+) (?P<vreme>[\d:]+) \[(?P<nivo>\w+)\] (?P<poruka>.+)"
for linija in log_linije:
    m = re.match(obrazac, linija)
    if m:
        nivo = m.group("nivo")
        ikona = {"INFO": "ℹ️", "ERROR": "❌", "WARNING": "⚠️"}.get(nivo, "•")
        print(f"  {ikona} {m.group('vreme')} [{nivo}] {m.group('poruka')}")
print("")

# --- 3. EKSTRAKCIJA URL-OVA ---
print("=== Ekstrakcija URL-ova ===")
html = """
<a href="https://skolica.rs">SKOLICA</a>
<a href="https://python.org">Python</a>
<a href="http://example.com/page?id=1">Test</a>
"""
urls = re.findall(r'href="(https?://[^"]+)"', html)
for url in urls:
    print(f"  🔗 {url}")
print("")

# --- 4. KOMPAJLIRANI REGEX ---
print("=== re.compile() ===")
email_pattern = re.compile(r"[\w.]+@[\w.]+\.\w+")
tekst = "Kontakt: vahid@skolica.rs ili enes@skolica.rs"
pronađeni = email_pattern.findall(tekst)
print(f"  Emailovi: {pronađeni}")

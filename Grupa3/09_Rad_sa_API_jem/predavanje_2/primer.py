#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 09_Rad_sa_API_jem / Predavanje 2
# Tema: POST, PUT, DELETE zahtevi sa requests
# =============================================================================

try:
    import requests
except ImportError:
    print("❌ pip install requests")
    exit(1)

BASE_URL = "https://jsonplaceholder.typicode.com"

# --- 1. POST — Kreiranje ---
print("=== POST (Kreiranje) ===")
novi_post = {
    "title": "ŠKOLICA Python Lekcija",
    "body": "Ovo je primer POST zahteva iz Python kursa.",
    "userId": 1
}
response = requests.post(f"{BASE_URL}/posts", json=novi_post)
print(f"  Status: {response.status_code}")
if response.status_code == 201:
    kreiran = response.json()
    print(f"  Kreiran ID: {kreiran['id']}")
    print(f"  Title: {kreiran['title']}")
print("")

# --- 2. PUT — Ažuriranje ---
print("=== PUT (Ažuriranje) ===")
azuriran = {
    "id": 1,
    "title": "Ažuriran naslov",
    "body": "Ažuriran sadržaj",
    "userId": 1
}
response = requests.put(f"{BASE_URL}/posts/1", json=azuriran)
print(f"  Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"  Title: {data['title']}")
print("")

# --- 3. DELETE — Brisanje ---
print("=== DELETE (Brisanje) ===")
response = requests.delete(f"{BASE_URL}/posts/1")
print(f"  Status: {response.status_code}")
if response.status_code == 200:
    print("  ✅ Resurs obrisan.")

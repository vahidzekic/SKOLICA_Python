#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 09_Rad_sa_API_jem / Predavanje 1
# Tema: Uvod u requests biblioteku, GET zahtevi
# =============================================================================

try:
    import requests
except ImportError:
    print("❌ Instalirajte requests: pip install requests")
    print("   Ovaj primer koristi javne API-je za demonstraciju.")
    exit(1)

# --- 1. JEDNOSTAVAN GET ZAHTEV ---
print("=== GET zahtev — JSONPlaceholder ===")
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(f"  Status kod: {response.status_code}")
print(f"  Content-Type: {response.headers.get('Content-Type')}")

if response.status_code == 200:
    post = response.json()
    print(f"  Title: {post['title'][:50]}...")
    print(f"  Body: {post['body'][:80]}...")
print("")

# --- 2. LISTA RESURSA ---
print("=== Lista korisnika ===")
users_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(users_url)

if response.status_code == 200:
    users = response.json()
    print(f"  Ukupno korisnika: {len(users)}")
    for user in users[:5]:
        print(f"  [{user['id']}] {user['name']} — {user['email']}")
print("")

# --- 3. OBRADA GREŠAKA ---
print("=== Obrada grešaka ===")
bad_url = "https://jsonplaceholder.typicode.com/posts/9999"
response = requests.get(bad_url)
print(f"  Status za nepostojeći resurs: {response.status_code}")
if response.status_code == 404:
    print("  ❌ Resurs nije pronađen!")

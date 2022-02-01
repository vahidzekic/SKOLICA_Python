#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 09_Rad_sa_API_jem / Predavanje 3
# Tema: Query parametri, session, timeout, praktičan primer
# =============================================================================

try:
    import requests
except ImportError:
    print("❌ pip install requests")
    exit(1)

# --- 1. QUERY PARAMETRI ---
print("=== Query parametri ===")
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
response = requests.get(url, params=params)

if response.status_code == 200:
    postovi = response.json()
    print(f"  Postovi korisnika 1: {len(postovi)}")
    for p in postovi[:3]:
        print(f"  [{p['id']}] {p['title'][:40]}...")
print("")

# --- 2. SESSION ---
print("=== Session ===")
session = requests.Session()
session.headers.update({"Accept": "application/json"})

r1 = session.get(f"{url}/1")
r2 = session.get(f"{url}/2")
print(f"  Post 1: {r1.json()['title'][:40]}...")
print(f"  Post 2: {r2.json()['title'][:40]}...")
session.close()
print("")

# --- 3. TIMEOUT I ERROR HANDLING ---
print("=== Timeout i greške ===")
try:
    response = requests.get("https://httpbin.org/delay/1", timeout=3)
    print(f"  Status: {response.status_code}")
except requests.Timeout:
    print("  ❌ Zahtev je istekao!")
except requests.ConnectionError:
    print("  ❌ Nema internet konekcije!")
except requests.RequestException as e:
    print(f"  ❌ Greška: {e}")

# --- 4. KOMPLETNI CRUD PRIMER ---
print("\n=== Kompletni CRUD ===")
BASE = "https://jsonplaceholder.typicode.com/posts"

# Create
r = requests.post(BASE, json={"title": "Test", "body": "...", "userId": 1})
print(f"  CREATE: {r.status_code}")

# Read
r = requests.get(f"{BASE}/1")
print(f"  READ: {r.json()['title'][:30]}...")

# Update
r = requests.put(f"{BASE}/1", json={"title": "Updated"})
print(f"  UPDATE: {r.status_code}")

# Delete
r = requests.delete(f"{BASE}/1")
print(f"  DELETE: {r.status_code}")

#!/usr/bin/env python3
# Grupa4 / 09 / P2 â POST, PUT, DELETE
try:
    import requests
except ImportError:
    print("pip install requests"); exit(1)

BASE = "https://jsonplaceholder.typicode.com"

# POST
print("=== POST ===")
r = requests.post(f"{BASE}/posts", json={"title": "G4 Test", "body": "...", "userId": 1})
print(f"  Status: {r.status_code}, ID: {r.json().get('id')}")

# PUT
print("\n=== PUT ===")
r = requests.put(f"{BASE}/posts/1", json={"title": "Updated", "body": ".", "userId": 1})
print(f"  Status: {r.status_code}, Title: {r.json()['title']}")

# DELETE
print("\n=== DELETE ===")
r = requests.delete(f"{BASE}/posts/1")
print(f"  Status: {r.status_code}")
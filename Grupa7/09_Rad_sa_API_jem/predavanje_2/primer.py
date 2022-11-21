#!/usr/bin/env python3
# Grupa7 / 09 / P2 â POST/PUT/DELETE
try:
    import requests
except ImportError: print("pip install requests"); exit(1)

BASE = "https://jsonplaceholder.typicode.com"

print("=== POST ===")
r = requests.post(f"{BASE}/posts", json={"title": "G7 Trip", "body": "travel", "userId": 1})
print(f"  {r.status_code}, ID: {r.json().get('id')}")

print("\n=== PUT ===")
r = requests.put(f"{BASE}/posts/1", json={"title": "Updated Trip"})
print(f"  {r.status_code}, Title: {r.json()['title']}")

print("\n=== DELETE ===")
r = requests.delete(f"{BASE}/posts/1")
print(f"  {r.status_code}")
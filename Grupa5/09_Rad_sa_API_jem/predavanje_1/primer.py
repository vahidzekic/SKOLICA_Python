#!/usr/bin/env python3
# Grupa5 / 09 / P1 â GET
try:
    import requests
except ImportError: print("pip install requests"); exit(1)

print("=== GET korisnici ===")
r = requests.get("https://jsonplaceholder.typicode.com/users")
if r.ok:
    for u in r.json()[:5]:
        print(f"  [{u['id']}] {u['name']} â {u['email']}")

print("\n=== GET post ===")
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if r.ok: print(f"  {r.json()['title'][:50]}")

print("\n=== 404 ===")
r = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
print(f"  Status: {r.status_code}")
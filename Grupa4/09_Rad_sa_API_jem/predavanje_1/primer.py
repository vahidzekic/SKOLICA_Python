#!/usr/bin/env python3
# Grupa4 / 09 / P1 â GET
try:
    import requests
except ImportError:
    print("pip install requests"); exit(1)

print("=== GET korisnici ===")
r = requests.get("https://jsonplaceholder.typicode.com/users")
if r.ok:
    for u in r.json()[:5]:
        print(f"  [{u['id']}] {u['name']} â {u['email']}")

print("\n=== GET post ===")
r2 = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if r2.ok:
    print(f"  Title: {r2.json()['title'][:50]}")

print("\n=== 404 ===")
r3 = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
print(f"  Status: {r3.status_code}")
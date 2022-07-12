#!/usr/bin/env python3
# Grupa5 / 09 / P3 â Session, timeout
try:
    import requests
except ImportError: print("pip install requests"); exit(1)

BASE = "https://jsonplaceholder.typicode.com"

print("=== Session ===")
with requests.Session() as s:
    s.headers.update({"Accept": "application/json"})
    r1 = s.get(f"{BASE}/posts/1")
    r2 = s.get(f"{BASE}/posts/2")
    print(f"  1: {r1.json()['title'][:35]}...")
    print(f"  2: {r2.json()['title'][:35]}...")

print("\n=== Timeout ===")
try:
    r = requests.get("https://httpbin.org/delay/1", timeout=3)
    print(f"  OK: {r.status_code}")
except requests.Timeout: print("  Timeout!")
except requests.ConnectionError: print("  No connection!")

print("\n=== Query ===")
r = requests.get(f"{BASE}/comments", params={"postId": 1})
if r.ok: print(f"  Comments: {len(r.json())}")
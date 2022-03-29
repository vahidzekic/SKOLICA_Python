#!/usr/bin/env python3
# Grupa4 / 05 / P1 â Funkcije

def pozdrav(ime, rec="Zdravo"):
    return f"{rec}, {ime}!"

def kalkulator(a, b, op="+"):
    ops = {"+": a+b, "-": a-b, "*": a*b, "/": a/b if b else "ERR"}
    return ops.get(op, "??")

def statistika(*br):
    if not br: return {}
    return {"min": min(br), "max": max(br), "avg": sum(br)/len(br)}

print(pozdrav("Vahid"))
print(pozdrav("Kemo", "Äao"))
print(f"5+3 = {kalkulator(5, 3)}")
print(f"Stats: {statistika(4, 8, 15, 16, 23, 42)}")
#!/usr/bin/env python3
# Grupa4 / 04 / P1 â if/elif/else

poeni = int(input("Poeni (0-100): "))

if poeni >= 91: ocena, opis = 10, "Izvanredan"
elif poeni >= 81: ocena, opis = 9, "OdliÄan"
elif poeni >= 71: ocena, opis = 8, "Vrlo dobar"
elif poeni >= 61: ocena, opis = 7, "Dobar"
elif poeni >= 51: ocena, opis = 6, "Dovoljan"
else: ocena, opis = 5, "Nedovoljan"

print(f"Poeni: {poeni} -> Ocena: {ocena} ({opis})")
print(f"Status: {'PoloÅ¾io' if ocena >= 6 else 'Pao'}")

# LogiÄki operatori
godine = 25
ima_kartu = True
if godine >= 18 and ima_kartu:
    print("Pristup dozvoljen")
elif godine >= 18:
    print("Kupite kartu")
else:
    print("Maloletni")
#!/usr/bin/env python3
# Grupa6 / 04 / P1 â if/elif/else

print("=== MuziÄki Å¾anr ===")
bpm = int(input("BPM (tempo): "))

if bpm >= 170: zanr = "Drum & Bass"
elif bpm >= 128: zanr = "Techno"
elif bpm >= 100: zanr = "Pop/Dance"
elif bpm >= 70: zanr = "Rock"
elif bpm >= 50: zanr = "Ballad"
else: zanr = "Ambient"

print(f"BPM {bpm} -> {zanr}")

# LogiÄki
print("\n=== Pristup ===")
godine = 16
ima_id = True
if godine >= 18 or ima_id:
    print("Ulaz dozvoljen")
else:
    print("Zabranjen pristup")

print(f"15 je {'paran' if 15 % 2 == 0 else 'neparan'}")
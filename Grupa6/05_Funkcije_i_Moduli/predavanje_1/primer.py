#!/usr/bin/env python3
# Grupa6 / 05 / P1 â Funkcije

def formatiraj_trajanje(minuta):
    m = int(minuta)
    s = int((minuta - m) * 60)
    return f"{m}:{s:02d}"

def playlist_info(*pesme):
    if not pesme: return {}
    trajanja = [p[1] for p in pesme]
    return {"count": len(pesme), "total": sum(trajanja), "avg": sum(trajanja)/len(trajanja)}

def album_card(**kw):
    for k, v in kw.items():
        print(f"  {k}: {v}")

print(f"3.45 min = {formatiraj_trajanje(3.45)}")
print(f"5.55 min = {formatiraj_trajanje(5.55)}")

info = playlist_info(("Imagine", 3.03), ("Yesterday", 2.05), ("Hey Jude", 7.11))
print(f"\nPlaylist: {info}")

print("\nAlbum:")
album_card(naziv="Abbey Road", bend="Beatles", godina=1969)
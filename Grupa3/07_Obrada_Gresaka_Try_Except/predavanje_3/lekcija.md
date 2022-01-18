# Predavanje 3 — Logging i Debugging Obrasci

## 3.1 Logging modul

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug poruka")
logger.info("Informativna poruka")
logger.warning("Upozorenje")
logger.error("Greška")
logger.critical("Kritična greška")
```

## 3.2 Nivoi logovanja

| Nivo | Numerički | Upotreba |
|---|---|---|
| DEBUG | 10 | Detaljne info za debugging |
| INFO | 20 | Potvrda da stvari rade |
| WARNING | 30 | Nešto neočekivano |
| ERROR | 40 | Ozbiljan problem |
| CRITICAL | 50 | Program ne može nastaviti |

## Rezime
- `logging` umesto `print()` za produkcijski kod
- Konfigurisati nivo, format, i output (fajl/konzola)

# Predavanje 2 — Rad sa JSON Fajlovima

## 2.1 JSON u Python-u

`json` modul konvertuje Python ↔ JSON:

| JSON → Python | Python → JSON |
|---|---|
| `json.load(fajl)` | `json.dump(objekat, fajl)` |
| `json.loads(string)` | `json.dumps(objekat)` |

## 2.2 Mapiranje tipova

| JSON | Python |
|---|---|
| `object {}` | `dict` |
| `array []` | `list` |
| `string` | `str` |
| `number` | `int/float` |
| `true/false` | `True/False` |
| `null` | `None` |

## Rezime
- `json.dump()` piše u fajl, `json.dumps()` u string
- `indent=4` za formatiranje, `ensure_ascii=False` za Unicode

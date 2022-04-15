#!/usr/bin/env python3
# Grupa4 / 07 / P3 â Logging
import logging, os
os.makedirs('data', exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)-8s] %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('data/g4.log', encoding='utf-8')]
)
log = logging.getLogger('G4')

log.debug('Debug poruka')
log.info('App pokrenuta')
log.warning('Disk 85%')
log.error('DB konekcija odbijena')

def unos(prompt, tip=int, n=3):
    for i in range(1, n+1):
        try:
            v = tip(input(prompt))
            log.info(f'Unos: {v}')
            return v
        except ValueError:
            log.warning(f'Los unos ({i}/{n})')
    log.error('Max pokuÅ¡aja')
    return None

print(f'Unos: {unos("Broj: ")}')
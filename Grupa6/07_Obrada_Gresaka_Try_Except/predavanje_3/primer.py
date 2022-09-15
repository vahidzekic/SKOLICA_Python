#!/usr/bin/env python3
# Grupa6 / 07 / P3 â Logging
import logging, os
os.makedirs('data', exist_ok=True)
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s [%(levelname)-8s] %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('data/g6.log', encoding='utf-8')])
log = logging.getLogger('G6')

log.debug('Debug')
log.info('App start')
log.warning('Disk 85%')
log.error('File not found')

def siguran(prompt, tip=int, n=3):
    for i in range(1, n+1):
        try:
            v = tip(input(prompt))
            log.info(f'Unos: {v}')
            return v
        except ValueError:
            log.warning(f'LoÅ¡ unos ({i}/{n})')
    return None

print(f'Rezultat: {siguran("Broj: ")}')
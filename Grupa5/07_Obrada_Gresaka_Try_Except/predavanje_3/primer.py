#!/usr/bin/env python3
# Grupa5 / 07 / P3 â Logging
import logging, os
os.makedirs('data', exist_ok=True)
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s [%(levelname)-8s] %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('data/g5.log', encoding='utf-8')])
log = logging.getLogger('G5')

log.debug('Debug info')
log.info('App start')
log.warning('Disk 90%')
log.error('Network error')

def siguran(prompt, tip=int, n=3):
    for i in range(1, n+1):
        try:
            v = tip(input(prompt))
            log.info(f'Unos: {v}')
            return v
        except ValueError:
            log.warning(f'LoÅ¡ unos ({i}/{n})')
    return None

print(f'Broj: {siguran("Unesi: ")}')
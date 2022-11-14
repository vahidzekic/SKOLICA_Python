#!/usr/bin/env python3
# Grupa7 / 07 / P3 â Logging
import logging, os
os.makedirs('data', exist_ok=True)
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s [%(levelname)-8s] %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('data/g7.log', encoding='utf-8')])
log = logging.getLogger('G7')

log.debug('Debug')
log.info('Trip planner start')
log.warning('BudÅ¾et nizak')
log.error('Destinacija not found')

def siguran(prompt, tip=float, n=3):
    for i in range(1, n+1):
        try:
            v = tip(input(prompt))
            log.info(f'Unos: {v}')
            return v
        except ValueError:
            log.warning(f'LoÅ¡ unos ({i}/{n})')
    return None

print(f'BudÅ¾et: {siguran("EUR: ")}')
from pathlib import Path

import requests


def scrape_gutenburg(num, start, end, name):
    res = requests.get(f'https://www.gutenberg.org/cache/epub/{num}/pg{num}.txt')
    data = str(res.text).replace('\r', '')
    data = data.split(start)[-1].split(end)[0]
    (Path.cwd() / 'data' / name / 'clean.txt').write_text(data)

scrape_gutenburg(216, 'Translated by James Legge', 'End of the Project Gutenberg', 'tao')

from pathlib import Path

import requests


res = requests.get('https://www.gutenberg.org/cache/epub/164/pg164.txt')
data = str(res.text).replace('\r', '')
data = data.split('PART ONE')[-1].split('End of the Project Gutenberg')[0]
(Path.cwd() / 'data' / 'jules-verne' / 'clean.txt').write_text(data)

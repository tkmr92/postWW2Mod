import re

files = []

with open('./country_tags/00_countries.txt', 'r') as FILE:
    for line in FILE.readlines():
        if "#" in line:
            continue
        file = re.search('countries\/\w*\s*\w*.txt', line)
        open(file.group(), 'a').close()
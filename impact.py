# Collin Pearce 100%
import json

N = int(input())

publicationData = json.loads(input())

publications = {}

for publication in publicationData['publications']:
    publications[publication['publicationNumber']] = {'years': [], 'citable': 0, 'citations': 0, 'name': publication['publicationTitle']}
    for articleCount in publication['articleCounts']:
        publications[publication['publicationNumber']]['years'].append(articleCount['year'])
        publications[publication['publicationNumber']]['citable'] += int(articleCount['articleCount'])
# print(publications)

for i in range(N - 1):
    data = json.loads(input())
    for citation in data['paperCitations']['ieee']:
        if citation['publicationNumber'] in publications:
            if citation['year'] in publications[citation['publicationNumber']]['years']:
                publications[citation['publicationNumber']]['citations'] += 1

outputs = {}
for publication in publications.values():
    outputs.setdefault(f"{publication['citations']/publication['citable']:.2f}", [])
    outputs[f"{publication['citations']/publication['citable']:.2f}"].append(publication['name'])

for key in reversed(sorted(outputs.keys())):
    for val in sorted(outputs[key]):
        print(val,": ", key, sep = '')

# parse JSON input, score each publication then print in reversed order
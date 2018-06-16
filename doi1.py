import urllib
import requests
from crossref.restful import Works, Etiquette
my_etiquette = Etiquette('Wikipedia quality bachelor thesis', '1.0', 'null', 'qamilnowak@gmail.com')
str(my_etiquette)
works = Works()
works = Works(etiquette=my_etiquette)
def fetch_issns():
    with open('doienkoniec2.tsv') as f:
        lines = f.readlines()[1:]  # skip line 1 (table headers)

        articles = []
        for line in lines:
            articles.append(
                {
                 'issn': line.split('\t')[0].strip(),
                })

        return articles

def retrieve_data(doi_encoded, article):
        return {
            'issn': article['issn'],
            'enc': doi_encoded['ISSN'][0] if 'ISSN' in doi_encoded else 'null',
        }


def fetch_results():
    results = []

    for article in fetch_issns():
        if works.doi(article['issn']) is not None:
                doi_encoded = works.doi(article['issn'])
        else:doi_encoded='null'
        print('[INFO] Parsed DOI: ' + str(article['issn']))
        results.append(
            retrieve_data(doi_encoded, article))

    return results


def write_to_file(results):
    with open('doienkoniec2_ext.tsv', 'w') as f:
        for result in results:
            for index, item in enumerate(result):
                if index < (len(result) - 1):
                    f.write(str(result[item]) + '\t')
                else:
                    f.write(str(result[item]) + '\n')

    print('INFO] Wrote to file')


results = fetch_results()
write_to_file(results)

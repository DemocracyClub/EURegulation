import os
import csv
import requests

in_file = open('eu-legislation-subjects.csv')

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.8",
}

def mk_folder_for_id(uuid):
    path = os.path.join(*[
        'docs',
        uuid[:2],
    ])
    os.makedirs(path, exist_ok=True)
    return path


for line in csv.DictReader(in_file):
    print(line['REG_CELLAR_ID'].split('/')[-1])
    uuid = line['REG_CELLAR_ID'].split('/')[-1]
    path = mk_folder_for_id(uuid)
    with open("{}/{}.html".format(path, uuid), 'w') as f:
        req = requests.get(line['REG_CELLAR_ID'], headers=HEADERS)
        f.write(req.text)

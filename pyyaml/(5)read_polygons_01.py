# read_categories.py file

import yaml

# with open(r'E:\data\categories.yaml') as file:
with open("polygons.yaml") as file:
    # поменял кодировку на cp866 - пошло !!!

    documents = yaml.full_load(file)

    for item, doc in documents.items():
        print(item, ":", doc)

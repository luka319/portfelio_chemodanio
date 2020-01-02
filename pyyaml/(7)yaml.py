import yaml

with open(r'fruits(7).yaml') as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)

    sort_file = yaml.dump(doc, sort_keys=True)
    print(sort_file)

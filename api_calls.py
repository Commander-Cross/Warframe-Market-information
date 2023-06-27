import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def get_all_items_from_web():
    items = requests.get("https://api.warframe.market/v1/items")
    if(items.status_code == 200):
        with open("items.json", 'w') as output:
            json.dump(items.json(), output)

def load_items():
    with open("items.json", 'r') as item_file:
        items = json.load(item_file)
        
    return items


# get_all_items_from_web()

item_list = load_items()

#jprint(item_list)
print(item_list[])


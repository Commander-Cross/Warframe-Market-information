import requests
import json
import time

#Json Pretty Printer
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# Gets a list of all items from the web and saves it into items.json
def get_all_items_from_web():
    items = requests.get("https://api.warframe.market/v1/items")
    if(items.status_code == 200):
        with open("./sources/items.json", 'w') as output:
            json.dump(items.json(), output)

def load_items():
    with open("./sources/items.json", 'r') as item_file:
        items = json.load(item_file)
        
    return items



# Gets a list of all npcs from the web 
#NPCs usually mean enemy units, like gineer lancer
def get_all_npcs_from_web():
    npcs = requests.get("https://api.warframe.market/v1/npc")
    if(npcs.status_code == 200):
        with open("./sources/npcs.json", 'w') as output:
            json.dump(npcs.json(), output)

def load_npcs():
    with open("./sources/npcs.json", 'r') as npc_file:
        npcs = json.load(npc_file)
        
    return npcs


#gets a list of all missions this is typically mission types, not nodes
def get_all_missions_from_web():
    missions = requests.get("https://api.warframe.market/v1/missions")
    if(missions.status_code == 200):
        with open("./sources/missions.json", 'w') as output:
            json.dump(missions.json(), output)

def load_missions():
    with open("./sources/missions.json", 'r') as missions_file:
        misisons = json.load(missions_file)
        
    return misisons


#locations are typically named nodes
def get_all_locations_from_web():
    locations = requests.get("https://api.warframe.market/v1/locations")
    if(locations.status_code == 200):
        with open("./sources/locations.json", 'w') as output:
            json.dump(locations.json(), output)

def load_locations():
    with open("./sources/locations.json", 'r') as location_file:
        locations = json.load(location_file)
        
    return locations


############################################################################################################################################################
# Variables
############################################################################################################################################################
requests_per_second = 2.5
delay = 1 / requests_per_second



############################################################################################################################################################
# NO NEED TO RUN THIS UNLESS AN UPDATE HAS HAPPENED
# Gets information on all warframe data items
############################################################################################################################################################

def update_information():
    get_all_items_from_web()
    time.sleep(delay)
    get_all_npcs_from_web()
    time.sleep(delay)
    get_all_locations_from_web()
    time.sleep(delay)
    get_all_missions_from_web()

def url_names(item_list):
    urls = []
    for url_name in item_list['payload']['items']:
        urls.append(url_name['url_name'])
    return urls



# item_list = load_items()
# npc_list = load_npcs()
# mission_list = load_missions()
# location_list = load_locations()





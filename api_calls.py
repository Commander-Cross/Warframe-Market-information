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
        with open("./game_info/items.json", 'w') as output:
            json.dump(items.json(), output)

def load_items():
    with open("./game_info/items.json", 'r') as item_file:
        items = json.load(item_file)
        
    return items



# Gets a list of all npcs from the web 
#NPCs usually mean enemy units, like gineer lancer
def get_all_npcs_from_web():
    npcs = requests.get("https://api.warframe.market/v1/npc")
    if(npcs.status_code == 200):
        with open("./game_info/npcs.json", 'w') as output:
            json.dump(npcs.json(), output)

def load_npcs():
    with open("./game_info/npcs.json", 'r') as npc_file:
        npcs = json.load(npc_file)
        
    return npcs


#gets a list of all missions this is typically mission types, not nodes
def get_all_missions_from_web():
    missions = requests.get("https://api.warframe.market/v1/missions")
    if(missions.status_code == 200):
        with open("./game_info/missions.json", 'w') as output:
            json.dump(missions.json(), output)

def load_missions():
    with open("./game_info/missions.json", 'r') as missions_file:
        misisons = json.load(missions_file)
        
    return misisons



#locations are typically named nodes
def get_all_locations_from_web():
    locations = requests.get("https://api.warframe.market/v1/locations")
    if(locations.status_code == 200):
        with open("./game_info/locations.json", 'w') as output:
            json.dump(locations.json(), output)

def load_locations():
    with open("./game_info/locations.json", 'r') as location_file:
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
    time.sleep(delay)
    items = load_items()
    item_urls = url_names(items)
    for item in item_urls:
        get_drop_sources_from_web(item)
        time.sleep(delay)



############ gets all item urls from a nested dictionary of all items#######################
def url_names(item_list):
    urls = []
    for url_name in item_list['payload']['items']:
        urls.append(url_name['url_name'])
    return urls





#################### Gets all orders of an item and saves it to the folder ##########################
def get_order_info(item_url):
    save_loc = f"./order_info/{item_url}.json"
    orders = requests.get(f"https://api.warframe.market/v1/items/{item_url}/orders")
    if(orders.status_code == 200):
        with open(save_loc, "w") as sav_file:
            json.dump(orders.json(), sav_file)
            time.sleep(delay)



def load_orders():
    pass


################################# seems useful for later ###############################################
def find_id(dictionary, target_id):
    for key, value in dictionary.items():
        if key == 'id' and value == target_id:
            return dictionary
        elif isinstance(value, dict):
            result = find_id(value, target_id)
            if result is not None:
                return result
    return None


######### Gets all the drop sources of a given item from the web
def get_drop_sources_from_web(item_url):
    sources = requests.get(f"https://api.warframe.market/v1/items/{item_url}/dropsources")
    if(sources.status_code == 200):
        with open(f"./drop_sources/{item_url}.json", 'w') as output:
            json.dump(sources.json(), output)
            time.sleep(delay)

#later use
def load_drop_source(item_url):
    with open(f"./drop_sources/{item_url}.json", 'r') as drop_sources:
        sources = json.load(drop_sources)
        
    return sources



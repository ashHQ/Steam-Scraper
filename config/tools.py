import json


_config = {
    "url": "https://store.steampowered.com/specials",
    "container":
        {
            "name": "store_sale_divs",
            "selector": 'div[class*="salepreviewwidgets_StoreSaleWidgetContainer"]',
            "match": "all",
            "type": "node"
        }
    ,
    "item": [
        {
            "name": "title",
            "selector": 'div[class*=StoreSaleWidgetTitle]',
            "match": "first",
            "type": "text"
        }
    ]
}
def get_config(load_from_file=False):
    if load_from_file:
        with open("config.json","r") as f:
            return json.load(f)

    return _config


def generate_config():
    with open("config.json","w") as f:
        json.dump(_config, f, indent=4)

if __name__ == "__main__":
    generate_config()
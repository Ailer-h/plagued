from modules.json_tools import get_dict

def get_item_list(list_tag: str) -> list | dict | None:
    return get_dict("./data/items.json").get(list_tag, None)

rarities: dict | None = get_item_list("rarities_accepted")

class Item:
    def __init__(self, item_name: str, item_id: str, item_rarity: str = "common", max_stack: int = 10, slots_taken: int = 1):

        self.item_name = item_name
        self.item_id = item_id

        if item_rarity not in rarities['rarities_accepted']:
            item_rarity = "common"

        self.item_rarity = item_rarity

        self.quantity = 0
        self.slots_taken = slots_taken

        if slots_taken > 1:
            self.max_stack = 1
        
        else:
            self.max_stack = max_stack

    def pickup(self, quantity: int = 1):
        if self.quantity + quantity >= self.max_stack:
            print(f"You can't pickup more than {self.max_stack} {self.item_name}")
        
        self.quantity += quantity

    def drop(self, quantity: int = 1):
        if self.quantity - quantity < 0:
            print(f"You can't drop more {self.item_name} than you have")
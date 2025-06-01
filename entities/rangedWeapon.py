from item import Item
from modules.json_tools import get_dict

rarities: dict = get_dict("./data/items.json")

class RangedWeapon(Item):
    def __init__(self, item_name: str, item_id: str, weapon_stats: dict, item_rarity: str = "common"):
        super().__init__(item_name, item_id, item_rarity, max_stack = 1)

        self.range = weapon_stats.get("range", 10)
        self.damage_range = weapon_stats.get("damage_range", (1, 6))
        self.damage_type = weapon_stats.get("damage_type", "piercing")
        self.max_durability = weapon_stats.get("max_durability", 75)
        self.durability = weapon_stats.get("durability", self.max_durability)

        self.max_ammo = weapon_stats.get("max_ammo", 10)
        self.ammo = weapon_stats.get("ammo", self.max_ammo)

        self.type_ammo = weapon_stats.get("type_ammo", "short_bullet")

        self.crit_chance = weapon_stats.get("crit_chance", 7)
        self.crit_multiplier = weapon_stats.get("crit_multiplier", 1.5)

    def shoot(self) -> None:
        pass

    def reload(self) -> None:
        pass
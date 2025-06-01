from item import Item

class MeleeWeapon(Item):
    def __init__(self, item_name: str, item_id: str, weapon_stats: dict, item_rarity: str = "common"):
        super().__init__(item_name, item_id, item_rarity, max_stack = 1)

        self.range = weapon_stats.get("range", 2)
        self.damage_range = weapon_stats.get("damage_range", (1, 6))
        self.damage_type = weapon_stats.get("damage_type", "cutting")
        self.max_durability = weapon_stats.get("max_durability", 75)
        self.durability = weapon_stats.get("durability", self.max_durability)

        self.crit_chance = weapon_stats.get("crit_chance", 5)
        self.crit_multiplier = weapon_stats.get("crit_multiplier", 2)

    def attack(self) -> None:
        pass

    def feint(self) -> None:
        pass
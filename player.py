from class_handler import get_class

# Player class for the game
class Player:
    def __init__(self, name:str, player_class:str):
        
        # Handles class info
        class_data = get_class(player_class)
        
        self.player_class = class_data["class_name"]

        # Gets the attr and stats of the player based on class
        self.name = name
        self.max_hp = 100 + class_data["hp_increment"]
        self.current_hp = 100 + class_data["hp_increment"]
        self.lvl = 1
        self.xp = 0

        # Player stats
        self.stats = {
            "str": class_data["base_stats"]["str"],
            "thg": class_data["base_stats"]["thg"],
            "int": class_data["base_stats"]["int"],
            "chr": class_data["base_stats"]["chr"],
            "sns": class_data["base_stats"]["sns"],
            "agi": class_data["base_stats"]["agi"]
        }

        # This part is still a WIP
        self.inventory = []
        self.skills = {}
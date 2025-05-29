from modules.json_tools import get_dict

classes_path: str = r"data/classes.json"

# Finds the player class on the classes file and returns its info
def get_class(player_class: str):

    data: dict = get_dict(classes_path)
    
    if player_class.lower() not in data.keys():
        player_class = "combatent"

    return data[player_class]

# Returns the stats of a class in a nice str one-liner format
def get_stats(player_class: str):
    stats: dict = get_class(player_class)["base_stats"]

    stats_line: str = ""
    for key in stats.keys():
        stats_line += f"{key.upper()} - {stats[key]} | "

    return stats_line[:-3:]
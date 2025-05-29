from entities.player import Player
import modules.json_tools as json_tools
from modules.class_handler import get_stats
from modules.input_handler import get_int
import colorama
from colorama import Fore

classes_path: str = r"data/classes.json"
games_path: str = r"data/games.json"

colorama.init(autoreset=True)

# Function responsible for getting input on player info
# STILL GOTTA EDIT IT
def create_character():

    print("What's the name of your character?")
    name = input("> ")
    
    print("Chose a class for your character:")

    # Prints all classes and stores its names in a list
    class_data: dict = json_tools.get_dict(classes_path)
    classes: list[str] = []
    for i, key in enumerate(class_data, start=1):
        item = class_data[key]
        stats = get_stats(key)

        classes.append(item['class_name'])

        # Nice formating for class info
        print(f"{i}. {item['class_name'].capitalize()}")
        print(f"   - {item['class_description']}")
        print(f"   - Stats: {stats}")

    # Gets classname based on index. If index invalid, defaults to combatent
    player_class: int = get_int("> ", default=0) - 1

    print()

    if player_class < 0 or player_class > len(classes) - 1:
        player_class = 0

    char = Player(name, classes[player_class])

    # Shows user the character they created
    print("Alright. Here is your character!")
    print(f"{char.name} - LVL:{char.lvl} {char.player_class.capitalize()}")
    print(f"HP: {Fore.RED + str(char.current_hp)}/{str(char.max_hp) + Fore.WHITE} | EXP: {Fore.GREEN + str(char.xp)}")
    print(get_stats(char.player_class))

    return char

def display_game_slots(slots: dict):

    for key in slots.keys():

        slot = slots[key]

        if not slot:
            game_info: str = "--Empty--"
        
        else:
            game_info: str = f"{slot['player_data']['name']} ({slot['player_data']['player_class']}) - Days Played: {slot['game_data']['time_played']}"

        print(f"{key} - {game_info}")

def save_game(char: Player, slot: str):
    
    data: dict = {
        "game_data": {
            "time_played": 0
        },

        "player_data": {
            "player_class": char.player_class,
            "name": char.name,
            "max_hp": char.max_hp,
            "current_hp": char.current_hp,
            "lvl": char.lvl,
            "xp": char.xp,
            "stat": char.stats,
            "inventory": char.inventory,
            "skills": char.skills
        }
    }
    
    slots: dict = json_tools.get_dict(games_path)

    slots[slot] = data
    json_tools.update_json(slots, games_path)

    return data

# Function that loads a save
def load_save() -> dict:
    print("Select a save to load.")

    slots: dict = json_tools.get_dict(games_path)
    display_game_slots(slots)

    print("\nSelect a slot to load.")
    selected_slot = get_int("> ", repeat=True, bounds={"min": 1, "max": len(slots)}) - 1

    return slots[list(slots.keys())[selected_slot]]

# Function that prompts the user to save a char
def new_game():
    print("Create a new save.")

    slots: dict = json_tools.get_dict(games_path)
    display_game_slots(slots)

    print("\nSelect a slot.")
    selected_slot = get_int("> ", repeat=True, bounds={"min": 1, "max": len(slots)}) - 1

    game_slot: str = list(slots.keys())[selected_slot]

    new_char = create_character()
    game_data: dict = save_game(new_char, game_slot)

    return game_data

#Function that prompts the user to delete one save
def delete_save():
    print("Manage your saves.")

    slots: dict = json_tools.get_dict(games_path)
    display_game_slots(slots)

    print("\nSelect a slot to delete.")
    selected_slot = get_int("> ", repeat=True, bounds={"min": 1, "max": len(slots)}) - 1

    print(f"\nAre you sure you want to delete {Fore.BLUE + list(slots.keys())[selected_slot] + Fore.WHITE}?")
    print(Fore.RED + "This action is ireversible!")

    user_opt = input("Y/N > ")

    if user_opt.lower() != "y":
        print("Canceling...")
        return

    slots[list(slots.keys())[selected_slot]].clear()

    json_tools.update_json(slots, games_path)
    
    
# Function that starts the game menu
def menu():

    while True:

        print(f"Welcome to {Fore.RED}Plagued{Fore.WHITE}!")
        print("Select an option to start!")
        print("1. Load Game | 2. New Game | 3. Manage Saves | 4. Quit")

        user_opt = get_int("> ", repeat=True, bounds={"min": 1, "max": 4})

        print()

        if user_opt == 1:
            return load_save()

        elif user_opt == 2:
            return new_game()

        elif user_opt == 3:
            delete_save()

        else:
            print("Quitting...")
            return

# Function that runs the game
def run_game():
    game_data = menu()

menu()
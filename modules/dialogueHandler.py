from modules.json_tools import get_dict, update_json
from time import sleep
from os import path

#Handles the display of dialogues in the game
class DialogueHandler:

    def __init__(self, dialogue_path: str | None = None) -> None:
        self.dialogue_path: str | None = dialogue_path

        if not self.dialogue_path:
            self.dialogue_db: dict = {}
            return

        if not path.isfile(self.dialogue_path):
            self.dialogue_db: dict = {}
            return

        self.dialogue_db: dict = get_dict(self.dialogue_path)
        self.skip_dialogues: bool = False

    #Sets the file that should be used to find the dialogues
    def set_dialogue_path(self, dialogue_path: str) -> None:
        if not path.isfile(dialogue_path):
            print(f"File {dialogue_path} not found!")
            return

        self.dialogue_path = dialogue_path
        self.dialogue_db = get_dict(self.dialogue_path)

    def set_skip_dialogue(self, skip_state: bool) -> None:
        self.skip_dialogues = skip_state

    #Runs a dialogue from the database
    def run_dialogue(self, dialogue_id: str) -> None:
        if dialogue_id not in self.dialogue_db.keys():
            print(f"Dialogue {dialogue_id} not found on the database.")
            return
        
        dialogue: dict = self.dialogue_db[dialogue_id]

        print()

        for i, line in enumerate(dialogue['text']):
            print(line)

            default_delay = dialogue['default_delay']
            delay: float | str = dialogue['delay'].get(str(i), default_delay)

            if isinstance(delay, str):
                input(delay)
            
            elif not self.skip_dialogues:
                sleep(delay)

#Handles the process of creating dialogues
class DialogueEditor:

    def __init__(self, dialogue_path: str | None = None) -> None:
        self.dialogue_path: str | None = dialogue_path

        if not self.dialogue_path:
            self.dialogue_db: dict = {}
            return

        if not path.isfile(self.dialogue_path):
            self.dialogue_db: dict = {}
            return

        self.dialogue_db: dict = get_dict(self.dialogue_path)

    #Sets the file that should be used to find the files
    def set_dialogue_path(self, dialogue_path: str) -> None:
        if not path.isfile(dialogue_path):
            print(f"File {dialogue_path} not found!")
            return

        self.dialogue_path = dialogue_path
        self.dialogue_db = get_dict(self.dialogue_path)

    #Reloads the dialogue database from the file (use after edits)
    def reload_dialogue_db(self) -> None:
        if not self.dialogue_path or not path.isfile(self.dialogue_path):
            self.dialogue_db: dict = {}
            return
        
        self.dialogue_db = get_dict(self.dialogue_path)

    #Gets info about a dialogue for debugging
    def get_dialogue_info(self, dialogue_id: str) -> str:
        if dialogue_id not in self.dialogue_db.keys():
            print(f"Dialogue {dialogue_id} not found on the database.")
            return "Dialogue not found"
        
        dialogue: dict = self.dialogue_db[dialogue_id]

        dialogue_info = [
            f"Dialogue ID: {dialogue_id}",
            f"Dialogue Type: {dialogue['type']}",
            f"Dialogue default delay: {dialogue['default_delay']}",
            f"This dialogue has {len(dialogue['text'])} lines."
        ]

        return "\n".join(dialogue_info)

    #Gets the text for a dialogue from a txt file
    def get_dialogue_text(self, txt_path: str) -> list:
        if not path.isfile(txt_path):
            print(f"File {txt_path} not found!")
            return []
        
        txt_lines = []

        with open(txt_path, 'r', encoding='utf-8') as file:
            txt_lines = file.readlines()

        remove_breaks = lambda x: x.strip("\n")

        txt_lines = list(filter(None,map(remove_breaks, txt_lines)))

        return txt_lines


    #Creates a new dialogue
    def create_dialogue(self, dialogue_id: str, dialogue_info: dict) -> None:
        if dialogue_id in self.dialogue_db.keys():
            print(f"Dialogue {dialogue_id} already exists. Use 'edit_dialogue' instead.")
            return
        
        if not self.dialogue_path or not path.isfile(self.dialogue_path):
            print("You don't have a valid dialogue database. Please create one first.")
            return
        
        if "type" not in dialogue_info.keys():
            dialogue_info['type'] = "generic_dialogue"

        if "default_delay" not in dialogue_info.keys():
            dialogue_info['default_delay'] = 1

        if "delay" not in dialogue_info.keys():
            dialogue_info['delay'] = {}

        if "txt_path" not in dialogue_info.keys():
            dialogue_info['text'] = []
        
        else:
            dialogue_info['text'] = self.get_dialogue_text(dialogue_info['txt_path'])
            dialogue_info.pop("txt_path", None)

        self.dialogue_db[dialogue_id] = dialogue_info
        update_json(self.dialogue_db, self.dialogue_path)
        self.reload_dialogue_db()

    #Updates an existing dialogue
    def edit_dialogue(self, dialogue_id: str, dialogue_info: dict) -> None:
        if dialogue_id not in self.dialogue_db.keys():
            print(f"Dialogue {dialogue_id} not found on the database. Use 'create_dialogue' instead.")
            return
        
        if not self.dialogue_path or not path.isfile(self.dialogue_path):
            print("You don't have a valid dialogue database. Please create one first.")
            return

        dialogue: dict = self.dialogue_db[dialogue_id]

        if "type" in dialogue_info.keys():
            dialogue['type'] = dialogue_info['type']

        if "default_delay" in dialogue_info.keys():
            dialogue['default_delay'] = dialogue_info['default_delay']

        if "delay" in dialogue_info.keys():
            dialogue['delay'] = dialogue_info['delay']
        
        if "txt_path" in dialogue_info.keys():
            dialogue['text'] = self.get_dialogue_text(dialogue_info['txt_path'])

        self.dialogue_db[dialogue_id] = dialogue
        update_json(self.dialogue_db, self.dialogue_path)
        self.reload_dialogue_db()
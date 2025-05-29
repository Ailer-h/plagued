from modules.json_tools import get_dict
from time import sleep

class DialogueHandler:

    def __init__(self, dialogue_path: str | None = None):
        self.dialogue_path: str | None = dialogue_path

        if self.dialogue_path:
            self.dialogue_db: dict = get_dict(self.dialogue_path)

        else:
            self.dialogue_db: dict = {}

    def set_dialogue_path(self, dialogue_path: str):
        self.dialogue_path = dialogue_path
        self.dialogue_db = get_dict(self.dialogue_path)

    def run_dialogue(self, dialogue_id: str):
        if dialogue_id not in self.dialogue_db.keys():
            print(f"Dialogue {dialogue_id} not found on the database.")
            return
        
        dialogue: dict = self.dialogue_db[dialogue_id]

        for i, line in enumerate(dialogue['text']):
            print(line)

            if str(i) not in dialogue['delay'].keys():
                sleep(dialogue['default_delay'])
                continue

            delay = dialogue['delay'][str(i)]

            if isinstance(delay, str):
                input(delay)
            
            else:
                sleep(delay)

    def get_dialogue_info(self, dialogue_id: str):
        if dialogue_id not in self.dialogue_db.keys():
            print(f"Dialogue {dialogue_id} not found on the database.")
            return
        
        dialogue: dict = self.dialogue_db[dialogue_id]

        print(f"Dialogue ID: {dialogue_id}")
        print(f"Dialogue type: {dialogue['type']}")
        print(f"Dialogue default delay: {dialogue['default_delay']}s")
        print(f"This dialogue has {len(dialogue['text'])} lines.")
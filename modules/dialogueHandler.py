from modules.json_tools import get_dict
from time import sleep

class DialogueHandler:

    def __init__(self, dialogue_path: str | None = None) -> None:
        self.dialogue_colors: dict = get_dict("./data/text_colors.json")
        self.dialogue_path: str | None = dialogue_path

        if self.dialogue_path:
            self.dialogue_db: dict = get_dict(self.dialogue_path)

        else:
            self.dialogue_db: dict = {}

    def set_dialogue_path(self, dialogue_path: str) -> None:
        self.dialogue_path = dialogue_path
        self.dialogue_db = get_dict(self.dialogue_path)

    def run_dialogue(self, dialogue_id: str) -> None:
        if dialogue_id not in self.dialogue_db.keys():
            print(f"Dialogue {dialogue_id} not found on the database.")
            return
        
        dialogue: dict = self.dialogue_db[dialogue_id]

        print()

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
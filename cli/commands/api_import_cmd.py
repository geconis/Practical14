from base import Command
from infra.api_genshin import GenshinAPI
from models.character import Character

class ImportAPICharacterCommand(Command):


    def __init__(self, context):
        super().__init__("import_api_char", "Import character from Genshin API", context)

    def execute(self, args):
        if len(args) < 1:
            print("Usage: import_api_char <name>")
            return

        name = args[0].lower()

        print(f"Downloading data for '{name}'...")

        data = GenshinAPI.get_character(name)
        if not data:
            print("Character not found in API.")
            return

        try:
            stats = data.get("stats", {})
            strength = int(stats.get("strength", 10))
            agility = int(stats.get("agility", 10))
            intelligence = int(stats.get("intelligence", 10))
        except:
            strength = agility = intelligence = 10 

        image_url = data.get("images", {}).get("icon", None)

        new_char = Character(
            name=name,
            strength=strength,
            agility=agility,
            intelligence=intelligence,
            image_url=image_url
        )

        self.context.characters[name] = new_char
        self.context.save_characters()

        print(f"Character '{name}' imported successfully!")

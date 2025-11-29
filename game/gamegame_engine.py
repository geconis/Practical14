from models.character import Character

class GameEngine:

    def __init__(self, characters):

        self.characters = characters
        self.history = []

    def start_game(self, player1_name, player2_name):
        self.player1 = self.characters.get(player1_name)
        self.player2 = self.characters.get(player2_name)

        if not self.player1 or not self.player2:
            print("One or both characters not found.")
            return False

        print(f"Starting game: {self.player1.name} vs {self.player2.name}")
        return True

    def perform_action(self, actor_name, action_type, target_name):
        actor = self.characters.get(actor_name)
        target = self.characters.get(target_name)

        if not actor or not target:
            print("Invalid actor or target.")
            return

        if action_type == "attack":
            damage = actor.strength
            target.health -= damage
            self.history.append(f"{actor.name} attacks {target.name} for {damage} damage")
            print(f"{actor.name} attacks {target.name} for {damage} damage")
        elif action_type == "heal":
            heal_amount = actor.intelligence
            target.health += heal_amount
            self.history.append(f"{actor.name} heals {target.name} for {heal_amount} HP")
            print(f"{actor.name} heals {target.name} for {heal_amount} HP")
        else:
            print("Unknown action")
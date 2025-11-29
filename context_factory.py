from text_system import TextContext
from character_context import CharacterContext
from game_context import GameContext
from cli.commands.text_cmds import get_text_commands
from cli.commands.api_cmds import get_api_commands
from cli.commands.char_catalog_cmds import ListCharactersCommand, ShowCharacterStatsCommand
from cli.commands.create_char_cmd import CreateCharacterCommand
from cli.commands.game_cmds import SelectCharacterCommand, StartGameCommand, ActCommand
from inventory_context import InventoryContext
from cli.commands.inventory_cmds import AddItemCommand, ListInventoryCommand
from cli.commands.api_import_cmd import ImportAPICharacterCommand


def create_context_and_commands(mode):

    if mode == "text":
        context = TextContext()
        commands = get_text_commands(context) + get_api_commands(context)
    elif mode == "chars":
        context = CharacterContext()
        commands = [
            ListCharactersCommand(context),
            ShowCharacterStatsCommand(context),
            CreateCharacterCommand(context),
            ImportAPICharacterCommand(context) 
    ] + get_api_commands(context)

    elif mode == "game":
        char_context = CharacterContext()
        context = GameContext(char_context.characters)
        commands = [
            SelectCharacterCommand(context),
            StartGameCommand(context),
            ActCommand(context)
        ]
    elif mode == "inventory":
        char_context = CharacterContext()
        context = InventoryContext(char_context)
        commands = [
            AddItemCommand(context),
            ListInventoryCommand(context)
        ]
    else:
        return None, None

    return context, commands

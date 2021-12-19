import json
import pprint
from loguru import logger
from tabulate import tabulate
from pydantic import BaseModel

from pyfinder.character import Character

_pp = pprint.PrettyPrinter(indent=4)
def pprint(*args, **kwargs):
    _pp.pprint(*args, **kwargs)

class PyfinderKernel():

    def __init__(self):
        self.character = Character()

    # -----------------------------------------------------------------------
    # Configuration File Management
    # -----------------------------------------------------------------------

    def load_from_file(self, character_json):
        logger.info(f"Loading character sheet from {character_json}")
        with open(character_json, 'r') as f:
            char_dict = json.load(f)
        logger.debug(char_dict)
        self.character = Character.parse_obj(char_dict)
        logger.info(f"Successfully loaded character sheet")

    def save_to_file(self, character_json):
        logger.info(f"Saving character sheet to {character_json}")
        with open(character_json, 'w') as f:
            json.dump(self.character.dict(), f, indent=4)
        logger.info(f"Successfully saved character sheet")

    # -----------------------------------------------------------------------
    # Helper Functions
    # -----------------------------------------------------------------------

    def _print_table(self, name, table, headers=[], tablefmt="fancy_grid"):
        print(f"\n{name}:")
        print(tabulate(table, headers=headers, tablefmt=tablefmt))
        print("")

    # -----------------------------------------------------------------------
    # Shell Commands
    # -----------------------------------------------------------------------

    def view(self, view_list):
        if view_list == []:
            view_list = [
                'ability_scores',
                'hit_points',
                'initiative',
                'armor_class'
            ]
        for table in view_list:
            try:
                func = getattr(self, 'view_' + table)
                func()
            except AttributeError:
                logger.error(f"Table view doesn't exist! : {table}")

    # -----------------------------------------------------------------------
    # View Type Commands
    # -----------------------------------------------------------------------

    def view_abs(self):
        self.view_ability_scores()

    def view_ability_scores(self):
        abscr = self.character.get_ability_scores()
        table = [[stat, *[v for k, v in values.items()]] for stat, values in abscr.items()]
        header = list(abscr.get('STR').keys())
        self._print_table("Ability Scores", table, header)

    def view_hp(self):
        self.view_hit_points()

    def view_hit_points(self):
        table = [[self.character.total_hit_points, self.character.current_hit_points]]
        header = ["Total", "Current"]
        self._print_table("Hit Points", table, header)

    def view_init(self):
        self.view_initiative()

    def view_initiative(self):
        self._print_table("Initiative", [[self.character.initiative]])

    def view_ac(self):
        self.view_armor_class()

    def view_armor_class(self):
        table = [
            ["AC", self.character.armor_class],
            ["Touch AC", self.character.touch_armor_class],
            ["Flat Footed AC", self.character.flat_footed_armor_class]
        ]
        header = ["Armor Class Type", "Value"]
        self._print_table("Armor Class", table, header)

    def view_dict(self):
        self.view_dictionary()

    def view_dictionary(self):
        pprint(self.character.dict())

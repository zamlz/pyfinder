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
    # Shell Commands
    # -----------------------------------------------------------------------

    def view(self, view_list):
        if view_list == []:
            view_list = ['abs', 'hp']
        for table in view_list:
            try:
                func = getattr(self, 'view_' + table)
                func()
            except AttributeError:
                logger.error(f"Table view doesn't exist! : {table}")

    def view_ability_scores(self):
        abscr = self.character.get_ability_scores()
        table = [[stat, *[v for k, v in values.items()]] for stat, values in abscr.items()]
        header = list(abscr.get('STR').keys())
        print("\nAbility Scores:")
        print(tabulate(table, header, tablefmt="fancy_grid"))
        print("")

    def view_abs(self):
        self.view_ability_scores()

    def view_hit_points(self):
        hp = self.character.get_hit_points()
        table = [[hp['total'], hp['current']]]
        header = list(hp.keys())
        print("\nHit Points:")
        print(tabulate(table, header, tablefmt="fancy_grid"))
        print("")

    def view_hp(self):
        self.view_hit_points()

    def view_dictionary(self):
        pprint(self.character.dict())

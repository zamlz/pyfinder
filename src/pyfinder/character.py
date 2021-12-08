

import json
import pprint
from loguru import logger
from tabulate import tabulate
from dataclasses import dataclass, asdict
from dacite import from_dict

import pyfinder.data as data

_pp = pprint.PrettyPrinter(indent=4)
def pprint(*args, **kwargs):
    _pp.pprint(*args, **kwargs)

@dataclass
class Character(object):
    personal_info: data.PersonalInfo = data.PersonalInfo()
    level_exp: data.LevelExperience = data.LevelExperience()
    ability_scores: data.AbilityScores = data.AbilityScores()
    hit_points: data.HitPoints = data.HitPoints()

    # -----------------------------------------------------------------------
    # Configuration File Management
    # -----------------------------------------------------------------------

    @classmethod
    def load_from_file(cls, character_json):
        logger.info(f"Loading character sheet from {character_json}")
        with open(character_json, 'r') as f:
            char_dict = json.load(f)
        logger.debug(char_dict)
        character = from_dict(data_class=cls, data=char_dict)
        logger.info(f"Successfully loaded character sheet")
        return character

    @classmethod
    def save_to_file(cls, character, character_json):
        logger.info(f"Saving character sheet to {character_json}")
        with open(character_json, 'w') as f:
            json.dump(asdict(character), f, indent=4)
        logger.info(f"Successfully saved character sheet")


    # -----------------------------------------------------------------------
    # GET_* FUNCTIONS:
    #   The purpose of these functions will be to collect base data values
    #   and compute their true values (after traits, items, etc. have been
    #   applied. In other words, this is how you must get the true values.
    # -----------------------------------------------------------------------

    def get_ability_scores(self):
        # add external and temporary buffs/debuffs
        external = {}
        temp = {}
        return self.ability_scores.get_dict(external=external, temp=temp)

    def get_hit_points(self):
        return self.hit_points.get_dict()

    # -----------------------------------------------------------------------
    # Shell Commands
    # -----------------------------------------------------------------------

    def view(self, view_list):
        if view_list == []:
            view_list = ['abs']
        for table in view_list:
            try:
                func = getattr(self, 'view_' + table)
                func()
            except AttributeError:
                logger.error(f"Table view doesn't exist! : {table}")

    def view_ability_scores(self):
        abscr = self.get_ability_scores()
        table = [[stat, *[v for k, v in values.items()]] for stat, values in abscr.items()]
        header = list(abscr.get('STR').keys())
        print("\nAbility Scores:")
        print(tabulate(table, header, tablefmt="fancy_grid"))
        print("")

    def view_abs(self):
        self.view_ability_scores()

    def view_hit_points(self):
        hp = self.get_hit_points()
        table = [[hp['total'], hp['current']]]
        header = list(hp.keys())
        print("\nHit Points:")
        print(tabulate(table, header, tablefmt="fancy_grid"))
        print("")

    def view_hp(self):
        self.view_hit_points()

    def view_dictionary(self):
        pprint(asdict(self))

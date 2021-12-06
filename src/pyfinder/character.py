
import json
import pprint
from loguru import logger
from dataclasses import dataclass, asdict
from dacite import from_dict

import pyfinder.data as data

_pp = pprint.PrettyPrinter(indent=4)
def pprint(*args, **kwargs):
    _pp.pprint(*args, **kwargs)

@dataclass
class Character(object):
    personal_info: data.PersonalInfo = data.PersonalInfo()
    ability_scores: data.AbilityScores = data.AbilityScores()

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

    def display_dict(self):
        pprint(asdict(self))

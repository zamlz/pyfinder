#!/usr/bin/env python3
"""
Contains all classes related to the player character
"""

import abc
import math
from typing import List
from tabulate import tabulate
from dataclasses import dataclass, field, asdict


class CharacterData(abc.ABC):
    pass

    def view(self):
        table = [[x,y] for x, y in asdict(self).items()]
        print(f"\n{type(self).__name__}:")
        print(tabulate(table, ["key", "value"], tablefmt="fancy_grid"))


@dataclass
class PersonalInfo(CharacterData):
    name: str = ""
    class_list: List[str] = field(default_factory=list)
    race: str = ""
    gender: str = ""
    height: str = ""
    weight: str = ""
    hair: str = ""
    eyes: str = ""
    age: int = 0
    alignment: str = ""
    homeland: str = ""
    deity: str = ""
    background: str = ""


@dataclass
class LevelExperience(CharacterData):
    level: int = 1
    experience: int = 0


@dataclass
class AbilityScores(CharacterData):
    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0

    def _get_base_modifier(self, ability: str):
        score = getattr(self, ability)
        return math.floor((score - 10) / 2)

    @property
    def strength_mod(self):
        return self._get_base_modifier("strength")

    @property
    def dexterity_mod(self):
        return self._get_base_modifier("dexterity")

    @property
    def constitution_mod(self):
        return self._get_base_modifier("constitution")

    @property
    def intelligence_mod(self):
        return self._get_base_modifier("intelligence")

    @property
    def wisdom_mod(self):
        return self._get_base_modifier("wisdom")

    @property
    def charisma_mod(self):
        return self._get_base_modifier("charisma")

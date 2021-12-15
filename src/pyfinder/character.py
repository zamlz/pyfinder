#!/usr/bin/env python3
"""
Contains all classes related to the player character
"""

import abc
import math
from typing import List
from pydantic import BaseModel

class PersonalInfo(BaseModel):
    name: str = ""
    class_list: List[str] = []
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

class LevelExperience(BaseModel):
    level: int = 1
    experience: int = 0

class AbilityScores(BaseModel):
    # These are the BASE stats
    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0

    def get_abs_dict(self, external={}, temp={}):
        ability_scores = {
            'STR': {'BASE': self.strength},
            'DEX': {'BASE': self.dexterity},
            'CON': {'BASE': self.constitution},
            'INT': {'BASE': self.intelligence},
            'WIS': {'BASE': self.wisdom},
            'CHA': {'BASE': self.charisma}
        }
        for stat in ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']:
            # Get Base
            total = ability_scores[stat]['BASE']
            # If external adjustments are permanent bonuses (like racial traits)
            if external:
                ext = external.get(stat, 0)
                total += ext
                ability_scores[stat]['EXTERNAL'] = ext
                ability_scores[stat]['TOTAL'] = total
            # compute the base modifier
            modifier = math.floor((total - 10) / 2)
            ability_scores[stat]['MODIFIER'] = modifier
            # if any temporary adjustments exist, apply them now
            if temp:
                tmp_bonus = temp.get(stat, 0)
                tmp_total = total + tmp_bonus
                tmp_modifier = math.floor((tmp_total - 10) / 2)
                ability_scores[stat]['TMP_BONUS'] = tmp_bonus
                ability_scores[stat]['TMP_TOTAL'] = tmp_total
                ability_scores[stat]['TMP_MODIFIER'] = tmp_modifier
        return ability_scores

class HitPoints(BaseModel):
    total: int = 0
    current: int = 0

    def update(self, value):
        self.current = min(self.total, self.current + value)

class Character(BaseModel):
    personal_info: PersonalInfo = PersonalInfo()
    level_exp: LevelExperience = LevelExperience()
    ability_scores: AbilityScores = AbilityScores()
    hit_points: HitPoints = HitPoints()

    def get_ability_scores(self):
        # add external and temporary buffs/debuffs
        external = {}
        temp = {}
        return self.ability_scores.get_abs_dict(external=external, temp=temp)

    def get_hit_points(self):
        return self.hit_points.dict()

import pyfinder.character as char

class TestAbilityScores():

    def test_ability_scores_get_abs_dict(self):
        abscores = char.AbilityScores.parse_obj({
            'strength': 5,
            'dexterity': 7,
            'constitution': 9,
            'intelligence': 20,
            'wisdom': 100,
            'charisma': 45,
        })
        external = {
            'STR': 5,
            'DEX': 0,
            'CON': -5
        }
        temp = {
            'CON': 3,
            'INT': 4,
            'WIS': -50
        }
        expected_dict = {
            'STR': {
                'BASE': 5,
                'EXTERNAL': 5,
                'TOTAL': 10,
                'MODIFIER': 0,
                'TMP_BONUS': 0,
                'TMP_TOTAL': 10,
                'TMP_MODIFIER': 0
            },
            'DEX': {
                'BASE': 7,
                'EXTERNAL': 0,
                'TOTAL': 7,
                'MODIFIER': -2,
                'TMP_BONUS': 0,
                'TMP_TOTAL': 7,
                'TMP_MODIFIER': -2
            },
            'CON': {
                'BASE': 9,
                'EXTERNAL': -5,
                'TOTAL': 4,
                'MODIFIER': -3,
                'TMP_BONUS': 3,
                'TMP_TOTAL': 7,
                'TMP_MODIFIER': -2,
            },
            'INT': {
                'BASE': 20,
                'EXTERNAL': 0,
                'TOTAL': 20,
                'MODIFIER': 5,
                'TMP_BONUS': 4,
                'TMP_TOTAL': 24,
                'TMP_MODIFIER': 7,
            },
            'WIS': {
                'BASE': 100,
                'EXTERNAL': 0,
                'TOTAL': 100,
                'MODIFIER': 45,
                'TMP_BONUS': -50,
                'TMP_TOTAL': 50,
                'TMP_MODIFIER': 20,
            },
            'CHA': {
                'BASE': 45,
                'EXTERNAL': 0,
                'TOTAL': 45,
                'MODIFIER': 17,
                'TMP_BONUS': 0,
                'TMP_TOTAL': 45,
                'TMP_MODIFIER': 17,
            },
        }
        assert expected_dict == abscores.get_abs_dict(external, temp)

class TestHitPoints():

    def test_update(self):
        hitpoints = char.HitPoints.parse_obj({
            'total': 84,
            'current': 36
        })
        hitpoints.update(10)
        assert hitpoints.current == 46
        hitpoints.update(-23)
        assert hitpoints.current == 23
        hitpoints.update(7)
        assert hitpoints.current == 30
        hitpoints.update(-40)
        assert hitpoints.current == -10
        hitpoints.update(100)
        assert hitpoints.current == 84
        assert hitpoints.current == hitpoints.total

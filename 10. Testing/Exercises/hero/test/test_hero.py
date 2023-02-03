from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):

    def test_hero_init(self):
        username = "Test"
        level = 3
        health = 15
        dmg = 3.56

        h = Hero(username, level, health, dmg)

        self.assertEqual(username, h.username)
        self.assertEqual(level, h.level)
        self.assertEqual(health, h.health)
        self.assertEqual(dmg, h.damage)

    def test_str_return_correct_string(self):
        h = Hero("T", 10, 100, 50)
        expected_result = f"Hero {h.username}: {h.level} lvl\n" \
                          f"Health: {h.health}\n" \
                          f"Damage: {h.damage}\n"

        result = str(h)

        self.assertEqual(expected_result, result)

    def test_battle_process_if_hero_attacks_himself(self):
        h = Hero("T", 10, 100, 50)
        with self.assertRaises(Exception) as ex:
            h.battle(h)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_hero_health_reaches_zero_or_below(self):
        h = Hero("T", 10, 100, 50)
        enemy = Hero("E", 10, 12, 11)
        for health in [0, -50]:
            h.health = 0

            with self.assertRaises(ValueError) as ex:
                h.battle(enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_returns_draw(self):
        h = Hero("V", 10, 20, 50)
        e = Hero("E", 10, 20, 50)

        result = h.battle(e)

        self.assertEqual("Draw", result)

    def test_battle_return_win_when_enemy_is_beaten(self):
        h = Hero("V", 10, 20, 50)
        e = Hero("E", 1, 2, 3)
        result = h.battle(e)

        self.assertEqual("You win", result)
        self.assertEqual(11, h.level)

    def test_if_battle_return_lose_if_enemy_wins(self):
        h = Hero("V", 1, 1, 1)
        e = Hero("E", 23, 100, 89)
        result = h.battle(e)
        self.assertEqual("You lose", result)
        self.assertEqual(24, e.level)

    def test_if_enemy_hero_is_less_than_0(self):
        h = Hero("T", 10, 100, 50)
        enemy = Hero("E", 10, 0, 11)
        for health in [0, -50]:
            enemy.health = 0

            with self.assertRaises(ValueError) as ex:
                h.battle(enemy)
            self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))


if __name__ == "__main__":
    main()

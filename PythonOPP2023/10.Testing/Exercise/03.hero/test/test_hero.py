from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.good_hero = Hero("good hero", 10, 100, 10)
        self.bad_hero = Hero("bad hero", 11, 110, 11)

    def test_initialization(self):  # I hope judge does test this cuz srsly...
        self.assertEqual("good hero", self.good_hero.username)
        self.assertEqual("bad hero", self.bad_hero.username)
        self.assertEqual(10, self.good_hero.level)
        self.assertEqual(11, self.bad_hero.level)
        self.assertEqual(100, self.good_hero.health)
        self.assertEqual(110, self.bad_hero.health)
        self.assertEqual(10, self.good_hero.damage)
        self.assertEqual(11, self.bad_hero.damage)

    def test_when_player_is_battling_themselves_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.good_hero.battle(self.good_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_when_player_has_0_or_less_hp_raises_exception(self):
        self.good_hero.health = 0
        with self.assertRaises(Exception) as exc:
            self.good_hero.battle(self.bad_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(exc.exception))

    def test_when_player_is_trying_to_fight_someone_with_0_or_less_hp_raises_exception(self):
        self.bad_hero.health = 0
        with self.assertRaises(Exception) as exc:
            self.good_hero.battle(self.bad_hero)
        self.assertEqual("You cannot fight bad hero. He needs to rest", str(exc.exception))

    def test_battle_leads_to_draw(self):
        self.bad_hero = Hero("bad hero", 10, 100, 10)
        self.assertEqual("Draw", self.good_hero.battle(self.bad_hero))
        self.assertEqual(0, self.bad_hero.health)
        self.assertEqual(0, self.good_hero.health)

    def test_battle_leads_to_player_winning(self):
        self.good_hero = Hero("good hero", 12, 125, 12)
        self.assertEqual("You win", self.good_hero.battle(self.bad_hero))
        self.assertEqual(-34, self.bad_hero.health)
        self.assertEqual(9, self.good_hero.health)
        self.assertEqual(13, self.good_hero.level)
        self.assertEqual(17, self.good_hero.damage)

    def test_battle_when_player_loses(self):
        self.assertEqual("You lose", self.good_hero.battle(self.bad_hero))
        self.assertEqual(-21, self.good_hero.health)
        self.assertEqual(15, self.bad_hero.health)
        self.assertEqual(12, self.bad_hero.level)
        self.assertEqual(16, self.bad_hero.damage)

    def test_string_method_returns_right_info(self):
        expected_msg_good_hero = f"Hero good hero: 10 lvl\nHealth: 100\nDamage: 10\n"
        expected_msg_bad_hero = f"Hero bad hero: 11 lvl\nHealth: 110\nDamage: 11\n"
        self.assertEqual(expected_msg_good_hero, self.good_hero.__str__())
        self.assertEqual(expected_msg_bad_hero, self.bad_hero.__str__())


if __name__ == '__main__':
    main()

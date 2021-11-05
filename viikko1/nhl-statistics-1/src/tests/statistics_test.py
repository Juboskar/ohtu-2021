import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  # 16
            Player("Lemieux", "PIT", 45, 54), # 99
            Player("Kurri",   "EDM", 37, 53), # 90
            Player("Yzerman", "DET", 42, 56), # 98
            Player("Gretzky", "EDM", 35, 89)  # 124
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")

    def test_search_not_found(self):
        self.assertEqual(self.statistics.search("Zajac"), None)
    
    def test_team(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)
    
    def test_top_scorers(self):
        self.assertEqual(len(self.statistics.top_scorers(3)), 3)
        self.assertEqual("Gretzky", self.statistics.top_scorers(2)[0].name)
        self.assertEqual("Lemieux", self.statistics.top_scorers(2)[1].name)
import unittest
from recorder.team import Team

class TestTeam(unittest.TestCase):
	def test_team_is_created_with_0_points(self):
		team = Team("Guinea", 0)
		self.assertEqual(team.name, "Guinea")
		self.assertEqual(team.score, 0)

	
import unittest
from teamlist import TeamList
from team import Team

class TestTeamList(unittest.TestCase):

	def test_add_team(self):
		team1 = Team("Guinea", 0)
		team2 = Team("Pig", 0)
		teamlist1 = TeamList()

		teamlist1.add_team(team1)
		self.assertEqual(len(teamlist1.teams), 1)
		teamlist1.add_team(team2)
		self.assertEqual(len(teamlist1.teams), 2)

	def test_get_scores(self):
		team1 = Team("Guinea", 0)
		team2 = Team("Pig", 0)
		teamlist1 = TeamList()

		teamlist1.add_team(team1)
		teamlist1.add_team(team2)

		self.assertEqual(teamlist1.get_score(team1.name), 0)
		self.assertEqual(teamlist1.get_score(team2.name), 0)

	def test_add_score(self):
		team1 = Team("Guinea", 0)
		teamlist1 = TeamList()

		teamlist1.add_team(team1)
		teamlist1.add_score("Guinea", 2)

		self.assertEqual(teamlist1.get_score(team1.name), 2)

		teamlist1.add_score("Guinea", 3)
		self.assertEqual(teamlist1.get_score(team1.name), 5)
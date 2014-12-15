"""DOCSTRING"""

class TeamList(object):
    def __init__(self):
        self.teams = {}

    def add_team(self, team):
        self.teams[team.name] = team.score

    def get_score(self, team_name):
        return self.teams.get(team_name)

    def add_score(self, team_name, score):
        prev_score = self.get_score(team_name)
        if score is not None:
            if prev_score is None:
                self.teams[team_name] = int(score) + 0
            else:
                self.teams[team_name] = int(score) + prev_score
        else:
            if prev_score is None:
                self.teams[team_name] = 0 + 0
            else:
                self.teams[team_name] = 0 + prev_score

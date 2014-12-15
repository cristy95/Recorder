Feature: Record and update scores of a basketball game

		As a user, I want to be able to record the scores for two teams
		and view the scores of both teams

Scenario: Record a score
		Given i visit the homepage
		And both teams have no score yet
		When I enter the following:
			|team_name	|score 		|
			|Guinea		|2			|
		Then I should see the following:
			|team_name 	|score 		|
			|Guinea		|2			|
			|Pig		|0			|


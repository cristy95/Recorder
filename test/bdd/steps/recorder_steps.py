from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp
from recorder_app import TEAMLIST, APP

@step(u'Given i visit the homepage')
def given_i_visit_the_homepage(step):
    """When visiting the homepage"""
    world.browser = TestApp(APP)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)

@step(u'And both teams have no score yet')
def and_both_teams_have_no_score_yet(step):
    assert_equal(TEAMLIST.get_score("Guinea"), None)
    assert_equal(TEAMLIST.get_score("Pig"), None)

@step(u'When I enter the following:')
def when_i_enter_the_following(step):
    for row in step.hashes:
    	if row['team_name'] is "Guinea":
    		form = world.response.forms['recorder-form1']
    		form['score'] = row['score']
    		world.form_response = form.submit()
    		assert_equal(world.form_resonse.status_code, 200)
    	else:
    		form = world.response.forms['recorder-form2']
    		form['score'] = row['score']
    		world.form_response = form.submit()
    		assert_equal(world.form_response.status_code, 200)

@step(u'Then I should see the following:')
def then_i_should_see_the_following(step):
	for row in step.hashes:
		if row['team_name'] is "Guinea":
			assert_in("Guinea: {}".format(row['score']), world.form_response.text)
	